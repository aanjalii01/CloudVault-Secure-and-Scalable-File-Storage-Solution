# ☁️ CloudVault: Secure and Scalable File Storage Solution

CloudVault is a Flask-based cloud storage system designed to provide a secure, scalable, and user-friendly platform for uploading, downloading, and managing files. It features role-based access control, file encryption, and AWS S3 integration for scalable storage.

## 🔐 Features

- 🧑‍💼 **Role-Based Access**: Admin and User roles with different permissions.
- 🗃️ **Secure File Management**: Upload, download, and delete files securely.
- ☁️ **AWS S3 Integration**: Store and retrieve files from AWS S3 buckets.
- 🧾 **User Authentication**: Secure login and registration system.
- 📁 **File Metadata Tracking**: Manage and track uploaded file details.
- 🧩 **Modular Code Structure**: Clean and scalable Flask application.


## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)
- **Cloud Storage**: AWS S3
- **Authentication**: Flask-Login
- **ORM**: SQLAlchemy

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- AWS credentials (if using AWS S3)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aanjalii01/CloudVault-Secure-and-Scalable-File-Storage-Solution.git
   cd CloudVault-Secure-and-Scalable-File-Storage-Solution
2. **Create and activate a virtual environment**:
  
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies**:

   pip install -r requirements.txt

4. **Configure AWS (Optional)**:

  AWS_ACCESS_KEY_ID=your_aws_access_key
  AWS_SECRET_ACCESS_KEY=your_aws_secret_key
  AWS_S3_BUCKET_NAME=your_bucket_name
  SECRET_KEY=your_flask_secret_key

5. **Run the application**:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask run


## 🧪 User Roles

**Admin**

- Can manage all files.
- Can delete files of any user.

**User**

- Can upload, download, and delete only their files.

## 📂 Folder Structure

CloudVault/
├── app/
│   ├── templates/
│   ├── static/
│   ├── routes.py
│   ├── models.py
│   └── ...
├── uploads/
├── requirements.txt
├── .env.example
└── run.py
