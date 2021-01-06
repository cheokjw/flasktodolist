from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

secretkey = "MdXzwwtT14Gh3"
app = Flask(__name__)
app.config["SECRET_KEY"] = secretkey

class UserForm(FlaskForm):
    name = StringField("Username/ Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

bootstrap = Bootstrap(app)

if __name__ == "__main__":
    app.run(debug = True)
