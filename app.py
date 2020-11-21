<<<<<<< HEAD
from profile import create_app
=======
from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta
from loged.coctel import coctel
from config.userInf import userInf
#import sqlalchemy
>>>>>>> e7e5d047defcc70f2240aaf455c5283df45e4c82

app = create_app()

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

=======
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
>>>>>>> e7e5d047defcc70f2240aaf455c5283df45e4c82
