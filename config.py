import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # General Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-in-production'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max upload size: 16 MB
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

    # Database configuration (SQLite in instance folder)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'cloudvault.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS S3 configuration
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME', '')
    AWS_S3_REGION = os.environ.get('AWS_S3_REGION', 'us-east-1')

    # Feature toggles (enable/disable features via env vars)
    USE_LOCAL_STORAGE = os.environ.get('USE_LOCAL_STORAGE', 'True') == 'True'
    ENABLE_ENCRYPTION = os.environ.get('ENABLE_ENCRYPTION', 'True') == 'True'
    ENABLE_AUDIT_LOGGING = os.environ.get('ENABLE_AUDIT_LOGGING', 'True') == 'True'
    ENABLE_CHUNKED_UPLOADS = os.environ.get('ENABLE_CHUNKED_UPLOADS', 'False') == 'True'
    ENABLE_STORAGE_QUOTAS = os.environ.get('ENABLE_STORAGE_QUOTAS', 'False') == 'True'
    ENABLE_CHATBOT = os.environ.get('ENABLE_CHATBOT', 'True') == 'True'

    # Audit logging config
    AUDIT_LOG_PATH = os.path.join(basedir, 'logs', 'audit.log')

    # Encryption key filepath (used in encryption utilities)
    SECRET_KEY_PATH = os.path.join(basedir, 'secret.key')

    # Storage quotas (in megabytes)
    DEFAULT_STORAGE_QUOTA_MB = 100  # Default storage quota per user (100 MB)
