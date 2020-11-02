from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta

app=Flask(__name__)
app.secret_key= "beberHastaLaInconsciencia"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        session.permanent = True
        user = request.form["Nombre"]
        pasword = request.form["Contraseña"]
        session["user"] = user
        
        return redirect(url_for("cocteles"))
    else:
        if "user" in session:
                        return redirect(url_for("cocteles"))
        return render_template('index.html')
    
@app.route("/cocteles")
def cocteles():
    if "user" in session:
#        user = session["user"]
        return render_template("cocteles.html")
    else:
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

if __name__== '__main__':
    app.run(debug=True)
