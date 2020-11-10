from flask import Blueprint,render_template, session, redirect, url_for
from loged.dataJSON import data
from loged.jsonDesc import info

coctel=Blueprint("coctel",__name__, static_folder="static",template_folder="templates")


@coctel.route("/cocteles", methods=["POST","GET"])
@coctel.route("/")
def cocteles():
    #if "user" in session:
        return render_template("cocteles.html", data=data)
    #else:
    #    return redirect(url_for("index"))

@coctel.route("/desc", methods=["POST","GET"])
def desc():
    #if "user" in session:
        return render_template("desc.html", desCoc=info)
    #else:
    #    return redirect(url_for("index"))
