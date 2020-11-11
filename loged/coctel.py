from flask import Blueprint,render_template, session, redirect, url_for, request
from loged.dataJSON import jsonSearch
from loged.jsonDesc import fjsonDesc
# from app import session

coctel=Blueprint("coctel",__name__, static_folder="static",template_folder="templates")


@coctel.route("/cocteles", methods=["POST","GET"])
@coctel.route("/", methods=["POST", "GET"])
def cocteles():
    #if "user" in session:
    if request.method=="POST":
        strSearch=request.form["search"]
        data=jsonSearch(strSearch)
        # if data["drinks"]==None
        return render_template("cocteles.html", data=data,se=strSearch)
    else:
        strSearch="margarita"
        data=jsonSearch(strSearch)
        return render_template("cocteles.html",data=data,se=strSearch)

@coctel.route("/desc", methods=["POST","GET"])
def desc():
    #if "user" in session:
    idCoctail=request.args.get('type')
    descCoctail=fjsonDesc(idCoctail)
    return render_template("desc.html", desCoc=descCoctail)
    #else:
    #    return redirect(url_for("index"))
