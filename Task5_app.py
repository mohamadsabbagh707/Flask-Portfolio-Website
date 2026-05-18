# Task 5
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask-Mohamad Alsabbagh!"

@app.route("/about")
def about():
    return "This is the About page-Mohamad Alsabbagh!"

if __name__ == "__main__":
    app.run(debug=True)