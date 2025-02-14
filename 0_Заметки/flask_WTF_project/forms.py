from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    message = TextAreaField("Сообщение", validators=[DataRequired()])
    submit = SubmitField("Отправить")
