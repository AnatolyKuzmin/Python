from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route("/")
def home():
    return "Добро пожаловать на главную страницу!"

@app.route("/users")
def users():
    users_list = [
        {"name": "Иван", "age": 25},
        {"name": "Мария", "age": 30},
        {"name": "Петр", "age": 35}
    ]
    return render_template("users.html", users=users_list)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Валидация данных
        errors = []
        if not username:
            errors.append("Имя пользователя обязательно.")
        if not email or "@" not in email:
            errors.append("Введите корректный email.")
        if not password or len(password) < 6:
            errors.append("Пароль должен содержать не менее 6 символов.")

        if errors:
            for error in errors:
                flash(error)
            return redirect(url_for("register"))

        # Здесь можно добавить логику для сохранения пользователя в базу данных
        flash(f"Пользователь {username} успешно зарегистрирован!")
        return redirect(url_for("home"))

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)