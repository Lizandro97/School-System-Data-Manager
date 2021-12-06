import webbrowser
from flask import Flask
from flask import render_template
from flask import request
from constants import data, forms
import pyodbc
from conn import Server


app = Flask(__name__)

connection = Server("ODBC Driver 17 for SQL server", "DESKTOP-6G8N2EK", "BDColegio2", "lizandro", "123456").connection()
database = "BDColegio2"
connection = pyodbc.connect(connection)




@app.route('/')
def index():
    return render_template("index.html", data=data)


@app.route('/matricula')
def matricula():
    return render_template("matricula.html", data=forms)


@app.route("/matricula/form-estudiante", methods=["GET", "POST"])
def form_estudiante():
    cursor = connection.cursor()
    req = request.form.keys()
    form = request.form
    attr = ""
    values = ""
    for i, element in enumerate(req):
        if i < len(req) - 1:
            attr += f'"{element}"' + ","
            if request.form[element] != "":
                values += f"'{request.form[element]}'" + ","
        else:
            attr += f'"{element}"'
            if request.form[element] != "":
                values += f"'{request.form[element]}'"

    query = f"INSERT INTO alumnos ({attr}) VALUES ({values})"
    try:
        cursor.execute(query)
        cursor.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()



    return render_template("form_estudiante.html", data=data)




if __name__ == '__main__':
    app.run()
