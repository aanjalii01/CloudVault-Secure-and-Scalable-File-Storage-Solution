from flask import Flask
from app.extensions import db, login_manager
from app.routes.auth import auth
from app.routes.main import main
from app.routes.files import files
from app.routes.chatbot import chatbot
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change for production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cloudvault.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(files)
    app.register_blueprint(chatbot)

    # Create upload folder if doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    return app
