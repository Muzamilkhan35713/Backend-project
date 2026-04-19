from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template,request, redirect, Blueprint, flash, url_for, jsonify
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from .models import User, Post
from . import db
from werkzeug.utils import secure_filename
import os


main =  Blueprint("main", __name__)


@main.context_processor
def inject_user():
    return dict(user=current_user)

@main.route("/")
def home():
    if current_user.is_authenticated:
        return redirect("/dashboard")
    return redirect("/register")

@main.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        existing_user = User.query.filter_by(name=name).first()
        if existing_user:
            flash("Username already exists")
            return redirect("/register")
        
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")


@main.route("/login", methods=["GET","POST"])
def login():
    if request.method =="POST":
        name = request.form["name"]
        password = request.form["password"]
        user = User.query.filter_by(name=name).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/dashboard")
        flash("Invalid username or password")
        return redirect("/login")

    return render_template("login.html")


@main.route("/dashboard")
@login_required
def dashboard():
    posts =Post.query.all()
    return render_template("dashboard.html", posts=posts)


@main.route("/create_post",methods=["GET","POST"])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_post = Post(title=title, content =content,user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/dashboard")
    return render_template("create_post.html")

@main.route("/post/<int:post_id>", methods=["GET","POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        flash("You are not authorized to edit this post")
        return redirect("/dashboard")
    
    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect("/dashboard")
    
    return render_template("edit_post.html", post=post)

@main.route("/delete_post/<int:post_id>")
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        flash("You are not authorized to delete this post")
        return redirect("/dashboard")
    db.session.delete(post)
    db.session.commit()
    return redirect("/dashboard")

@main.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    if request.method =="POST":
        file= request.files["profile_pic"]
        if file and file.filename != "":

            filename = secure_filename(file.filename)
            folder = os.path.join(main.root_path, "static/profile_pics")
            os.makedirs(folder, exist_ok=True)


            filepath = os.path.join(folder, filename)
            

            file.save(filepath)
            current_user.profile_pic = filename
            db.session.commit()
        return redirect("/profile")
    return render_template("profile.html")

@main.route("/updata", methods = ["GET","POST"])
@login_required
def updata():
    if request.method == "POST":
        name= request.form["name"]
        password =request.form["password"]
        existing_user = User.query.filter_by(name=name).first()
        if existing_user and existing_user.id != current_user.id:
            flash("Username already exists")
            return redirect("/updata")
        current_user.name=name
        current_user.password= generate_password_hash(password)
        db.session.commit()
        return redirect("/profile")
    return render_template("updata.html", user=current_user)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


def token_required(tonken):
    user = User.query.filter_by(api_token=tonken).first()
    if not user:
        return jsonify({"error": "Invalid or missing token"}), 401
    return user

@main.route("/api/secure_posts")
def secure_posts():
    token = request.headers.get("Authorization")
    user = token_required(token)

    if not user:
        return jsonify({"error": "Unauthorized access"}), 401
    posts = Post.query.filter_by(user_id=user.id).all()
    result = []
    for post in posts:
        result.append({
            "title": post.title,
            "content": post.content
        })
    return jsonify(result)

@main.route("/api/posts")
@login_required
def api_posts():
    post = Post.query.all()
    result = []

    for post in post:
        result.append({
           "id": post.id, 
           "title": post.title,
           "content": post.content,
           "author": post.author.name})
    return jsonify(result)


@main.route("/api/post/<int:post_id>")
@login_required
def api_single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.name
    })

@main.route("/api/create_post", methods=["POST"])
@login_required
def api_create_post():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    user_id = data.get("user_id")

    if not title or not content or not user_id:
        return jsonify({"error": "Missing required fields"}), 400
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "Post created successfully" })

@main.route("/api/delete_post/<int:post_id>", methods=["DELETE"])
@login_required
def api_delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"})

