from flask import Flask, render_template, request
from pwd_gen import pwdGenerator
import db

DB_PATH = "/home/allki/.web_python/database/site.db"

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/page_2", methods=["GET", "POST"])
def page_2():
    result = ""
    if request.method == "POST":
        password = request.form.get("pwd")
        salt = request.form.get("salt")
        num_char = request.form.get("num_char")

        if password !=None and salt !=None and num_char !=None:
            result = pwdGenerator(password, salt, num_char)

            db.write_db(DB_PATH, [(password, salt, num_char, result)])
    
    return render_template("page_2.html", data=result)

@app.route("/page_3")
def page_3():
    return render_template("page_3.html", data=db.read_db(DB_PATH))

# тут обрабатывается GET-запрос с параметрами
@app.route("/test")
def page_4():
    # v1 = request.args["var_1"]
    v1 = request.args.get("variable_1")
    v2 = request.args.get("variable_2")
    # return f"Hello from TEST. Var 1 = {v1}, Var 2 = {v2}"
    return render_template("test.html", var_1=v1, var_2=v2)

def create_app():
    db.create_db(DB_PATH)
    return app