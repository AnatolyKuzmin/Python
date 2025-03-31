import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Обязательная настройка для Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    # Отключаем сигналы изменения (для оптимизации)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Секретный ключ для сессий Flask
    SECRET_KEY = 'your-secret-key-here'