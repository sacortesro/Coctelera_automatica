from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta
#from dataJSON import data
from loged.coctel import coctel

app=Flask(__name__)
app.register_blueprint(coctel,url_prefix="/loged")
app.secret_key= "beberHastaLaInconsciencia"
app.permanent_session_lifetime = timedelta(minutes=15)

@app.route('/index', methods=["POST","GET"])
@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        session.permanent = False
        user = request.form["Nombre"]
        pasword = request.form["Contraseña"]
        session["user"] = user        
        return redirect(url_for("coctel.cocteles"))
    else:
        if "user" in session:
            return redirect(url_for("coctel.cocteles"))
        return render_template('index.html')

# @app.route("/cocteles", methods=["POST","GET"])
# def cocteles():
#     if "user" in session:
# #        user = session["user"]
#         return render_template("cocteles.html", data=data)
#     else:
#         return redirect(url_for("index"))

# @app.route("/desc")
# def desc():
#     if "user" in session:
#         return render_template("desc.html")
#     else:
#         return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

if __name__== '__main__':
    app.run(debug=True)
