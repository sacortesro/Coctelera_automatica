from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta
from loged.coctel import coctel
from config.userInf import userInf
#import sqlalchemy

app=Flask(__name__)
app.register_blueprint(coctel,url_prefix="/loged")
app.register_blueprint(userInf,url_prefix="/config")
app.secret_key= "beberHastaLaInconsciencia"
app.permanent_session_lifetime = timedelta(minutes=15)

@app.route('/index', methods=["POST","GET"])
@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        session.permanent = True
        user = request.form["Nombre"]
        pasword = request.form["Contrasena"]
        session["user"] = user
        return redirect(url_for("coctel.cocteles"))
    else:
        if "user" in session:
            return redirect(url_for("coctel.cocteles"))
        return render_template('index.html')

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=3134)
