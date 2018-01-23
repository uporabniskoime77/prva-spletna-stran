from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("domaca_stran.html")

@app.route("/druga_stran")
def druga():
    return render_template("druga_stran.html")

@app.route("/blog/<int:st_blog>")
def blog(st_blog):
    print("Dobil sem stevilo", st_blog)
    zadnji = request.cookies.get("blog_stevilka")
    result = render_template("blog.html", stevilka = st_blog, prej = zadnji)
    result = make_response(result)
    result.set_cookie("blog_stevilka", str (st_blog))
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0")
