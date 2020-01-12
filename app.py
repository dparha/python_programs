from flask import Flask, render_template, request

# api that uses index.html

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        greeting = "Hello World"
    elif request.method == "POST":
        greeting = "Hello %s" % request.form['name']
        
    return render_template("index.html", greeting=greeting)


if __name__ == '__main__':
    app.run()
