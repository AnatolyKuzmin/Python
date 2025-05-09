from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Инициализируем SQLAlchemy с приложением
    db.init_app(app)
    
    # Создаём таблицы (в реальном проекте используйте миграции!)
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)