from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

secretkey = "MdXzwwtT14Gh3"
app = Flask(__name__)
app.config["SECRET_KEY"] = secretkey #Flask form requires a secret key

class UserForm(FlaskForm): #Form class
    name = StringField("Username/ Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/", methods = ["GET", "POST"]) #methods argument allows Flask to handle POST request
def index():  
    form = UserForm() #call class func
    if form.validate_on_submit():
        session["name"] = form.name.data #giving the user session if form is submited
        return redirect(url_for("index"))
    return render_template("index.html", form = form, name = session.get("name"))

@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("index"))
    
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name) #name=name allows variable to be inserted into html template

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

bootstrap = Bootstrap(app)

if __name__ == "__main__":
    app.run(debug = True)
