from flask import Flask
from flask import render_template

app = Flask(__name__)


data = {
    "title": "Fe y Alegria",
    "nav_items": ["Home", "Enrollment", "Students", "Administration", "Library", "Resources"]
}


@app.route('/')
def hello_world():  # put application's code here
    global data
    return render_template("index.html", data=data)


@app.route('/friends')
def friends():
    return "My friends."


if __name__ == '__main__':
    app.run()
