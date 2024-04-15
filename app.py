import requests
from flask import Flask, request, render_template

app = Flask(__name__)

app.config["SECRET_KEY"] = "DSDSDSDSDSDSDDSD"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create_ticket/<int:user_id>', methods=['GET', 'POST'])
def create_ticket(user_id):
    if request.method == "POST":
        title = request.form.get('title')
        rows = request.form.get('rows')
        columns = request.form.get('columns')
        date = request.form.get('date')

        response = requests.post(
            'http://127.0.0.1:5000/api/tickets',
            json={'user_id': user_id, 'title': title, 'rows': rows, 'columns': columns, 'date': date}
        )
        if response.status_code == 201:
            return 'Квиток створено <a href="http://127.0.0.1:5000/">До меню</a>'
        else:
            return 'помилка <a href="http://127.0.0.1:5000/">До меню</a>'
    return render_template("create_ticket.html", user_id=user_id)


if __name__ == '__main__':
    app.run(port=5001)
