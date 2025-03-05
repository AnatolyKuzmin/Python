from flask import Flask

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route("/")
def home():
    return "Hello, World!"

# Запускаем приложение
if __name__ == "__main__":
    app.run(debug=True)