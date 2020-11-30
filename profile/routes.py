from flask import current_app as app
from flask import redirect, render_template, url_for, request

from .forms import SignupForm, LogInForm
from .usersDB import db, User

@app.route("/", methods=("GET", "POST"))

@app.route("/login", methods=("GET", "POST"))
def login():
    form1 = LogInForm()
    form2 = SignupForm()
    if form1.validate_on_submit():
        if form1.login_bt.data:
            return redirect(url_for('home_coctail.home'))
    elif form2.validate_on_submit():
        if form2.submit.data:
            return redirect(url_for('home_coctail.home'))
    else:
        return render_template("index.html", form1=form1, form2=form2)
        

@app.route("/mission", methods=("GET", "POST"))
def mission():
    form1 = LogInForm()
    form2 = SignupForm()
    if form1.validate_on_submit():
        if form1.login_bt.data:
            return redirect(url_for('home_coctail.home'))
    elif form2.validate_on_submit():
        if form2.submit.data:
            return redirect(url_for('home_coctail.home'))
    else:
        return render_template("mission.html", form1=form1, form2=form2)

@app.route("/contact", methods=("GET", "POST"))
def contact():
    form1 = LogInForm()
    form2 = SignupForm()
    if form1.validate_on_submit():
        if form1.login_bt.data:
            return redirect(url_for('home_coctail.home'))
    elif form2.validate_on_submit():
        if form2.submit.data:
            return redirect(url_for('home_coctail.home'))
    else:
        return render_template("contact.html", form1=form1, form2=form2)

@app.route("/signup", methods=("GET", "POST"))
def signUp():
    form2 = SignupForm()
    form1 = LogInForm()
    if form1.validate_on_submit():
        if form1.login_bt.data:
            return redirect(url_for('home_coctail.home'))
    else:
        return render_template("signUp.html", form= form2, form1=form1, form2=form2)