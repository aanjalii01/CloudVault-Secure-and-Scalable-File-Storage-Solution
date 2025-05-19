from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory, abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = None  # Suppress default login message

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'admin' or 'user'
    files = db.relationship('File', backref='owner', lazy=True)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def roles_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated_view(*args, **kwargs):
            if current_user.role not in roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated_view
    return wrapper

@app.route('/')
@login_required
def index():
    if current_user.role == 'admin':
        files = File.query.all()
    else:
        files = File.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', files=files)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        flash('Invalid credentials!', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(request.url)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    new_file = File(filename=file.filename, user_id=current_user.id)
    db.session.add(new_file)
    db.session.commit()

    flash('File uploaded successfully', 'success')
    return redirect(url_for('index'))

@app.route('/download/<filename>')
@login_required
def download_file(filename):
    file = File.query.filter_by(filename=filename).first()
    if file and (file.user_id == current_user.id or current_user.role == 'admin'):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    flash('You do not have permission to download this file', 'danger')
    return redirect(url_for('index'))

@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    file = File.query.filter_by(filename=filename).first()
    if file and (file.user_id == current_user.id or current_user.role == 'admin'):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        db.session.delete(file)
        db.session.commit()
        flash('File deleted successfully', 'success')
    else:
        flash('You do not have permission to delete this file', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)