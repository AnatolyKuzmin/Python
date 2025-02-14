from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Привет, это главная страница!"
    items = ["Элемент 1", "Элемент 2", "Элемент 3"]
    return render_template('index.html', title=title, items=items)

if __name__ == '__main__':
    app.run(debug=True)
