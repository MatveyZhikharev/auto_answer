from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def index():
    professions = {"title": "Анкета",
                   "surname": "Жихарев",
                   "name": "Матвей",
                   "education": "Андреевич",
                   "profession": "Генерал",
                   "sex": "male",
                   "motivation": "Марс наш!",
                   "ready": "True"}
    return render_template('auto_answer.html', **professions)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
