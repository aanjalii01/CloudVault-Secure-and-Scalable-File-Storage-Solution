from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db, login_manager

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)  # used for login
    email = db.Column(db.String(120), unique=True, nullable=False)    # still kept for info
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')  # roles: 'user' or 'admin'
    
    # One-to-many relationship: one user can own many files
    files = db.relationship('File', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Flask-Login user loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)  # path where file is saved
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign key linking file to user.id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
