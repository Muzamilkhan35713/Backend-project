🧩 Flask Blog & API Backend
🔐 Authentication • 📝 Posts • 🌐 REST API • 📁 File Uploads
<p align="center"> <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask"> <img src="https://img.shields.io/badge/Database-MySQL-blue?style=for-the-badge&logo=mysql"> <img src="https://img.shields.io/badge/Auth-Flask--Login-green?style=for-the-badge"> <img src="https://img.shields.io/badge/API-REST-orange?style=for-the-badge"> </p> <p align="center"> <b>A full-featured Flask backend with authentication, blog system, API endpoints, and profile management.</b> </p>
🚀 Overview

This project is a Flask-based backend application that provides:

🔐 Secure user authentication system
📝 Blog post creation and management
👤 User profile handling (with image uploads)
🔑 Token-based API access
🌐 RESTful API endpoints

It is designed for learning, backend practice, and as a foundation for full-stack applications.

⚙️ Core Features
🔐 Authentication System
User registration & login
Password hashing using werkzeug.security
Session management via Flask-Login
Protected routes (@login_required)
📝 Blog Management
Create, edit, and delete posts
User-specific post ownership
Dashboard displaying all posts
👤 User Profile
Update username & password
Upload profile pictures
Secure file handling
🌐 REST API
Get all posts
Get single post
Create post via API
Delete post via API
Token-based secure endpoint
🧠 Tech Stack
Backend: Flask
Database: MySQL
ORM: SQLAlchemy
Authentication: Flask-Login
Security: Werkzeug (password hashing)
📂 Project Structure
project/
│── app/
│   ├── __init__.py      # App factory & config
│   ├── models.py        # Database models
│   ├── routes.py        # Application routes
│── templates/           # HTML templates
│── static/              # Static files (profile pics)
│── run.py               # Entry point
🧑‍💻 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/flask-blog-backend.git
cd flask-blog-backend
2️⃣ Install Dependencies
pip install flask flask_sqlalchemy flask_login pymysql
3️⃣ Configure Database

Update your database URI in config:

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost:3306/db_name"
4️⃣ Run Application
python run.py
🔑 API Endpoints
📌 Public / Authenticated
Method	Endpoint	Description
GET	/api/posts	Get all posts
GET	/api/post/<id>	Get single post
POST	/api/create_post	Create new post
DELETE	/api/delete_post/<id>	Delete post
🔐 Token-Protected
Method	Endpoint	Description
GET	/api/secure_posts	Get user-specific posts using API token

📌 Example Header:

Authorization: your_api_token_here
🖥️ Features in UI (HTML)
Register & Login صفحات
Dashboard with posts
Create/Edit forms
Profile page with image upload
⚠️ Security Notes
Passwords are hashed before storage
File uploads are secured using secure_filename
Token-based authentication implemented

⚠️ Important:
This project uses a hardcoded secret key and DB credentials — replace them in production.

🛣️ Future Improvements
🔒 JWT Authentication
📊 Pagination for posts
❤️ Like/Comment system
📁 Cloud image storage (AWS S3, etc.)
⚡ API rate limiting
🧪 Unit & integration tests
🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit pull requests.

⭐ Support

If you found this useful:

⭐ Star the repository
🍴 Fork it
🧠 Share improvements
👨‍💻 Author

Muhammad Muzamil khan
Backend Developer | Flask Enthusiast 💻

📜 License

This project is licensed under the MIT License.
