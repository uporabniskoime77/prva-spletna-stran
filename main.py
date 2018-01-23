from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("domaca_stran.html")

@app.route("/druga_stran")
def druga():
    return render_template("druga_stran.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
