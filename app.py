from flask import Flask, render_template, request
from delete_emails import delete_emails

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        gmail = request.form["gmail"]
        password = request.form["password"]
        sender = request.form["sender"]
        result = delete_emails(gmail, password, sender)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
