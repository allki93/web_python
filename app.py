from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/page_2")
def page_2():
    return render_template("page_2.html")

@app.route("/page_3")
def page_3():
    return render_template("page_3.html")

def create_app():
    return app