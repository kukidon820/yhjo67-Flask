from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Form
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yhjo67yhjo67yhjo67yhjo67'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://test:test@localhost:5411/test')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('form'))


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':

        data_from_form = {}

        for key, value in request.form.items():
            if key.startswith('name') and value.strip():
                data_from_form[key] = value.strip()

        if data_from_form:
            new_form = Form(data=data_from_form)
            db.session.add(new_form)
            db.session.commit()
            flash('Форма сохранена!')
            return redirect(url_for('results'))
        else:
            flash("Ошибка! Заполните поле.")

    return render_template("forms.html")


@app.route('/results', methods=['GET'])
def results():
    forms = Form.query.all()
    return render_template("results.html", forms=forms)


if __name__ == '__main__':
    app.run(debug=True)
