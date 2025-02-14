from flask import Flask, render_template, flash, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Необходим для защиты от CSRF

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash(f'Сообщение отправлено от {name} ({email}): {message}')
        return redirect(url_for('contact'))  # Перенаправление после успешной отправки
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
