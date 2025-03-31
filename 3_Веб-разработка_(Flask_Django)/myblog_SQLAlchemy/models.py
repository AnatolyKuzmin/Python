from flask_sqlalchemy import SQLAlchemy

# Инициализируем SQLAlchemy без привязки к app (паттерн "Фабрика приложений")
db = SQLAlchemy()

class User(db.Model):
    """Модель пользователя"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Связь один-ко-многим (у пользователя много постов)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    """Модель поста блога"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    # Внешний ключ для связи с пользователем
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)