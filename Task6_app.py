from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Task 6"

# Task 6 - Template with one variable
@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)

# Task 6 - Multiple variables

@app.route("/info/<name>")
def info(name):
    age = 30
    program = "BISI"

    return render_template("info.html", name=name, age=age, program=program)

if __name__ == "__main__":
    app.run(debug=True, port=5001)