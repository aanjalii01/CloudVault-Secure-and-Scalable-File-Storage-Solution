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

### ✅ Prerequisites

- Python 3.7+
- pip (Python package manager)
- AWS S3 credentials (Access Key, Secret Key, Bucket Name)

---

📂 Project Structure
php
Copy code
CloudVault/
│
├── static/                 # CSS, JavaScript, other assets
├── templates/              # HTML files (Jinja2 templates)
├── uploads/                # Uploaded file storage (if local)
├── app.py                  # Main Flask app
├── models.py               # SQLAlchemy models
├── forms.py                # WTForms (Login, Upload)
├── chatbot.py              # Chatbot logic
├── s3_utils.py             # AWS S3 upload/download
├── requirements.txt
└── README.md

🧪 Testing
Test Type	Status	Notes
User Login	✅ Pass	Valid credentials tested
File Upload (S3)	✅ Pass	Files upload and download tested
Admin File Control	✅ Pass	Admin access to all files verified
Chatbot Integration	✅ Pass	Basic Q&A responses working
UI Responsiveness	✅ Pass	Works on desktop and tablets

📈 Future Enhancements
📱 Full mobile responsiveness

🧠 Smarter chatbot using NLP (e.g., OpenAI API)

🔐 MFA (Multi-Factor Authentication)

💾 File preview & versioning

🌍 Global deployment with CDN caching
