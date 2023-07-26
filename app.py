from flask import Flask, render_template, request
from pwd_gen import pwdGenerator

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
    
    return render_template("page_2.html", data=result)

@app.route("/page_3")
def page_3():
    return render_template("page_3.html")

# тут обрабатывается GET-запрос с параметрами
@app.route("/test")
def page_4():
    # v1 = request.args["var_1"]
    v1 = request.args.get("var_1")
    v2 = request.args.get("var_2")
    # return f"Hello from TEST. Var 1 = {v1}, Var 2 = {v2}"
    return render_template("test.html", variable_1=v1, variable_2=v2)

def create_app():
    return app