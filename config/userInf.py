from flask import Blueprint,render_template, session, redirect, url_for, request


userInf=Blueprint("userInf",__name__, static_folder="static",template_folder="templates")

@userInf.route("/", methods=["POST","GET"])
def regist():
    return render_template("sign_up.html")