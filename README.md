🧩 Flask Blog & API Backend
🔐 Authentication • 📝 Posts • 🌐 REST API • 📁 File Uploads
<p align="center"> <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask"> <img src="https://img.shields.io/badge/Database-MySQL-blue?style=for-the-badge&logo=mysql"> <img src="https://img.shields.io/badge/Auth-Flask--Login-green?style=for-the-badge"> <img src="https://img.shields.io/badge/API-REST-orange?style=for-the-badge"> </p> <p align="center"> <b>A full-featured Flask backend with authentication, blog system, API endpoints, and profile management.</b> </p>
<br>
🚀 Overview

This project is a Flask-based backend application that provides:

🔐 Secure user authentication system<br>
📝 Blog post creation and management<br>
👤 User profile handling (with image uploads)<br>
🔑 Token-based API access<br>
🌐 RESTful API endpoints

It is designed for learning, backend development practice, and as a foundation for full-stack applications.<br>
<br>
⚙️ Core Features<br>
🔐 Authentication System<br>
User registration & login<br>
Password hashing using werkzeug.security<br>
Session management via Flask-Login<br>
Protected routes (@login_required)<br><br>
📝 Blog Management<br>
Create, edit, and delete posts<br>
User-specific post ownership<br>
Dashboard displaying all posts<br><br>
👤 User Profile<br>
Update username & password<br>
Upload profile pictures<br>
Secure file handling<br><br>
🌐 REST API<br>
Get all posts<br>
Get single post<br>
Create post via API<br>
Delete post via API<br>
Token-based secure endpoint<br>

🧠 Tech Stack
Backend: Flask
Database: MySQL
ORM: SQLAlchemy
Authentication: Flask-Login
Security: Werkzeug<br><br>
## 📂 Project Structure

```bash
project/
│── app/
│   ├── __init__.py      # App factory & configuration
│   ├── models.py        # Database models
│   ├── routes.py        # Application routes
│── templates/           # HTML templates
│── static/              # Static files (e.g., profile pictures)
│── run.py               # Application entry point
```
🧑‍💻 Installation & Setup
1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/flask-blog-backend.git
cd flask-blog-backend
```
2️⃣ Install Dependencies
```
pip install flask flask_sqlalchemy flask_login pymysql
```
3️⃣ Configure Database
```
Update your database URI:

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost:3306/db_name"
```
4️⃣ Run Application
```
python run.py
```
🔑 API Endpoints<br>
📌 Public / Authenticated<br>
```
Method	Endpoint	Description
GET	/api/posts	Get all posts
GET	/api/post/<id>	Get single post
POST	/api/create_post	Create new post
DELETE	/api/delete_post/<id>	Delete post
```
🔐 Token-Protected
```
Method	Endpoint	Description
GET	/api/secure_posts	Get user-specific posts using API token
```
📌 Example Header:
```
Authorization: your_api_token_here
```
🖥️ Frontend (HTML)<br>
Register & Login pages<br>
Dashboard with posts<br>
Create/Edit forms<br>
Profile page with image upload<br><br>
⚠️ Security Notes<br>
Passwords are hashed before storage<br>
File uploads secured using secure_filename<br>
Token-based authentication implemented<br><br>

⚠️ Important:<br>
This project uses hardcoded credentials — use environment variables in production.<br><br>

🛣️ Future Improvements<br>
🔒 JWT Authentication<br>
📊 Pagination for posts<br>
❤️ Like/Comment system<br>
📁 Cloud storage (AWS S3, etc.)<br>
⚡ API rate limiting<br>
🧪 Testing (unit & integration)<br>
🤝 Contributing<br><br>

Contributions are welcome! Feel free to fork and submit pull requests.
<br>
⭐ Support
<br>

If you like this project:<br>

⭐ Star the repo<br>
🍴 Fork it<br>
🧠 Suggest improvements<br>
👨‍💻 Author<br>

Muhammad Muzamil Khan<br>
Backend Developer | Flask Enthusiast 💻<br>

📜 License<br>

This project is licensed under the MIT License.
