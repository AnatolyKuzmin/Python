from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Post, Comment

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "supersecretkey"

db.init_app(app)

@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)

@app.route("/post/create", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        if not title or not content:
            flash("Заголовок и текст поста обязательны!", "error")
        else:
            post = Post(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            flash("Пост успешно создан!", "success")
            return redirect(url_for("home"))

    return render_template("create_post.html")

@app.route("/post/<int:post_id>/comment", methods=["POST"])
def add_comment(post_id):
    content = request.form.get("content")

    if not content:
        flash("Комментарий не может быть пустым!", "error")
    else:
        comment = Comment(content=content, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash("Комментарий успешно добавлен!", "success")

    return redirect(url_for("view_post", post_id=post_id))

if __name__ == "__main__":
    app.run(debug=True)