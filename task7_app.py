from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        {"name": "Project Alpha", "completed": True},
        {"name": "Project Beta", "completed": False},
        {"name": "Project Gamma", "completed": True},
        {"name": "Project Delta", "completed": False},
        {"name": "Project Epsilon", "completed": True}
    ]

    return render_template("task7.html", name="Mohamad", projects=projects)

if __name__ == "__main__":
    app.run(debug=True, port=5002)