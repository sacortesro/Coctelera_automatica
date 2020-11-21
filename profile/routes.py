from flask import current_app as app
from flask import redirect, render_template, url_for, request

from .forms import SignupForm, LogInForm

@app.route("/", methods=("GET", "POST"))
@app.route("/login", methods=("GET", "POST"))
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.login_bt.data:
            return redirect(url_for('home_coctail.home'))
    # elif request.method == 'POST':
    #     if request.
    #     return redirect
    else:
        return render_template("index.html", form=form)

@app.route("/signup", methods=("GET", "POST"))
def signUp():
    form = SignupForm()
    return render_template("signUp.html", form=form)