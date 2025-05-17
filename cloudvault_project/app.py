from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory, abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from functools import wraps

# Initialize the Flask app and extensions
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for Flask-Login
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

# Initialize Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Roles required decorator
def roles_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated_view(*args, **kwargs):
            if current_user.role not in roles:
                abort(403)  # Forbidden
            return f(*args, **kwargs)
        return decorated_view
    return wrapper

# Home page route
@app.route('/')
@login_required
def index():
    files = File.query.filter_by(user_id=current_user.id).all()  # Get only files uploaded by the logged-in user
    return render_template('index.html', files=files)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid credentials!', 'danger')
    return render_template('login.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Upload file route
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
    
    # Save file to the uploads folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    # Create a File record in the database
    new_file = File(filename=file.filename, user_id=current_user.id)
    db.session.add(new_file)
    db.session.commit()
    
    flash('File uploaded successfully', 'success')
    return redirect(url_for('index'))

# Download file route
@app.route('/download/<filename>')
@login_required
def download_file(filename):
    file = File.query.filter_by(filename=filename, user_id=current_user.id).first()
    if not file:
        flash('You do not have permission to download this file', 'danger')
        return redirect(url_for('index'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Delete file route
@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    file = File.query.filter_by(filename=filename, user_id=current_user.id).first()
    if file:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        db.session.delete(file)
        db.session.commit()
        flash('File deleted successfully', 'success')
    else:
        flash('You do not have permission to delete this file', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Ensure that the app context is active when creating tables
    with app.app_context():
        db.create_all()  # Create the database tables
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
