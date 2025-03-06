from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Иван")

@app.route("/users")
def users():
    users_list = [
        {"name": "Иван", "age": 25},
        {"name": "Мария", "age": 30},
        {"name": "Петр", "age": 35}
    ]
    return render_template("users.html", users=users_list)

if __name__ == "__main__":
    app.run(debug=True)