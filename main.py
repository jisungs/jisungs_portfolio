from flask import Flask, render_template, request

import smtplib
import os

app = Flask(__name__)

# test line
@app.route('/', methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        data = request.form
        print(f"{data['name']} {data['email']} {data['phone']} {data['message']}")
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)

# send email is not prepared
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(os.environ.get("OWN_EMAIL"), os.environ.get("OWN_PASSWORD"))
        connection.sendmail(os.environ.get("OWN_EMAIL"), os.environ.get("OWN_EMAIL"), email_message)


if __name__ == "__main__":
    app.run(debug=True)
