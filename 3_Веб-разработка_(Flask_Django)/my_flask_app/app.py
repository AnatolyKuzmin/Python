from flask import Flask

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

# Запускаем приложение
if __name__ == "__main__":
    app.run(debug=True)