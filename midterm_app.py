from flask import Flask
from flask import request
from flask import render_template,url_for

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("login.html")
@sample.route("/registration")
def sub_main():
    return render_template("registration.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port = 5000)