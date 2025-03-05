from flask import Flask, request

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route("/")
def home():
    return "Hello, World!"

# Создаём маршрут с параметрами
@app.route("/user/<name>")
def greet_user(name):
    return f"Привет, {name}!"

# Обработка различных HTTP-методов
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Привет, {name} (POST)!"
    return """
        <form method="post">
            <label for="name">Имя:<label>
            <input type="text" id="name" name="name">
            <button type="submit">Отправить</button>
        </form>
    """

# Запускаем приложение
if __name__ == "__main__":
    app.run(debug=True)