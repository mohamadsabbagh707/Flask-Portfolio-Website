from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
from twilio.rest import Client

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("hello.html", name="Mohamad")


# ---------------- PROJECTS PAGE ----------------
@app.route("/projects")
def projects():
    projects = [
        {"name": "Project Alpha", "completed": True},
        {"name": "Project Beta", "completed": False},
        {"name": "Project Gamma", "completed": True},
        {"name": "Project Delta", "completed": False},
        {"name": "Project Epsilon", "completed": True}
    ]
    return render_template("task7.html", name="Mohamad", projects=projects)


# ---------------- EMAIL FUNCTION ----------------
def send_email(name, email, message):
    msg = EmailMessage()
    msg["Subject"] = "Portfolio Contact Message"
    msg["From"] = "mohamad.sabbagh707@gmail.com"
    msg["To"] = "mohamad.sabbagh707@gmail.com"

    msg.set_content(
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Message: {message}"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("mohamad.sabbagh707@gmail.com", "XXXXXXXXXXXXXXXXXXXXXXXX")  # for security reasons 
        server.send_message(msg)


# ---------------- SMS FUNCTION ---------
def send_sms(message):
    account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # for security reasons 
    auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # for security reasons 

    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_="+15799772464",
        to="+16132403573"
    )


# ---------------- CONTACT PAGE ----------------
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Try sending email
        try:
            send_email(name, email, message)
            email_status = "Email sent successfully!"
        except Exception as e:
            email_status = f"Email failed: {e}"

        # Try sending SMS
        try:
            send_sms(f"New message from {name}: {message}")
            sms_status = "SMS sent successfully!"
        except Exception as e:
            sms_status = f"SMS failed: {e}"

        return render_template(
            "contact.html",
            email_status=email_status,
            sms_status=sms_status
        )

    return render_template("contact.html")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)