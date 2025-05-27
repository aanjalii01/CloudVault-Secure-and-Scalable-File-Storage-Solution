# ☁️ CloudVault: Secure and Scalable File Storage Solution

CloudVault is a secure, user-friendly, and scalable cloud storage web application built using **Flask** and integrated with **AWS S3**. It enables users to upload, download, and manage files with role-based access control, file metadata tracking, and a built-in chatbot assistant for ease of use.

---

## 🔐 Features

- 🧑‍💼 **Role-Based Access Control**  
  Separate privileges for Admin and regular Users.

- ☁️ **AWS S3 Integration**  
  Files are stored and retrieved securely using Amazon S3 cloud storage.

- 🗂️ **File Upload, Download & Delete**  
  Each user can manage their own files; Admin can manage all.

- 🔐 **User Authentication System**  
  Secure login system using `Flask-Login`.

- 🧾 **File Metadata Tracking**  
  Track upload time, file type, and size.

- 🤖 **Chatbot Assistance**  
  Integrated chatbot to guide users during file management.

- 🧩 **Modular and Scalable Codebase**  
  Clean structure suitable for future expansion (e.g., database upgrade, AI chatbot).

---

## 🛠️ Tech Stack

| Layer      | Tools/Frameworks |
|------------|------------------|
| Frontend   | HTML, CSS, Bootstrap |
| Backend    | Python, Flask, Flask-Login |
| Database   | SQLite (easily switchable to PostgreSQL/MySQL) |
| Cloud      | AWS S3 (via `boto3`) |
| ORM        | SQLAlchemy |
| Bot        | Python-based chatbot (custom logic) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- AWS account with S3 access

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/aanjalii01/CloudVault-Secure-and-Scalable-File-Storage-Solution.git
   cd CloudVault-Secure-and-Scalable-File-Storage-Solution
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS Credentials**:

   - Set up your AWS credentials in the environment or configuration file to enable S3 integration.

5. **Initialize the database**:

   ```bash
   python create_db.py
   ```

6. **Run the application**:

   ```bash
   python run.py
   ```

7. **Access the application**:

   Open your web browser and navigate to `http://localhost:5000`.

## 📂 Project Structure

```
CloudVault/
├── app/
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   ├── __init__.py         # Initializes the Flask app
│   ├── routes.py           # Defines application routes
│   ├── models.py           # Database models
│   └── utils.py            # Utility functions
├── instance/
│   └── cloudvault.db       # SQLite database file
├── logs/                   # Application logs
├── migrations/             # Database migrations
├── config.py               # Configuration settings
├── create_db.py            # Script to initialize the database
├── run.py                  # Entry point to run the Flask app
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## ✅ Functionalities

- **User Registration and Authentication**: Secure user sign-up and login functionalities.
- **File Upload and Download**: Users can upload files to and download files from the cloud storage.
- **Admin Dashboard**: Admins can manage users and monitor file activities.
- **Activity Logs**: Tracks user activities for security and auditing purposes.

## 🧪 Testing & Validation

- **Authentication Tests**: Verified secure login and access control mechanisms.
- **File Handling Tests**: Ensured reliable file upload and download processes.
- **AWS S3 Integration Tests**: Confirmed successful storage and retrieval of files from S3.
- **User Interface Tests**: Validated responsiveness and usability of the web interface.

## 🔮 Future Enhancements

- **Two-Factor Authentication**: Enhance security with additional authentication layers.
- **File Versioning**: Implement version control for uploaded files.
- **Search Functionality**: Allow users to search for files within the storage system.
- **Sharing Capabilities**: Enable file sharing between users with appropriate permissions.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Developed as part of the Virtualization and Cloud Computiong course (CLOUD-IV-T012 ) at Graphic Era University.*


🔐 MFA (Multi-Factor Authentication)

💾 File preview & versioning

🌍 Global deployment with CDN caching
