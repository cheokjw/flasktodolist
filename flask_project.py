from flask import Flask, redirect, url_for, render_template, request,session

app = Flask(__name__)
app.secret_key = "moonlight123"

@app.route("/") #home page
def home():
    return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"]) #GET = requesting information from user while POST = posting information into website
def login():
    if request.method == "POST": #direct user into other pages if input is successful.  
        user = request.form["nm"]
        session["user"] = user #giving session to the user
        return redirect(url_for("user"))
    else: 
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("index.html", usr = user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)