from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from flask_login import login_required, logout_user, current_user, login_user

from .forms import SignupForm, LogInForm
from .usersDB import db, User
from . import login_manager





@app.route("/", methods=("GET", "POST"))
@app.route("/login", methods=("GET", "POST"))
def login():
    # Continuar a lista si el usuario esta logeado
    # if current_user.is_authenticated:
    #     return redirect(url_for('main_bp.dashboard'))

    formLogIn = LogInForm()
    if formLogIn.validate_on_submit():
        user = User.query.filter_by(username=formLogIn.name.data).first()
        if user and user.check_password(password=formLogIn.password.data):
            login_user(user)
            return redirect(url_for('home_coctail.home'))
        flash('Invalid username/password combination')
    return render_template("index.html", form1=formLogIn)
        

@app.route("/mission", methods=("GET", "POST"))
def mission():
    formLogIn = LogInForm()
    if formLogIn.validate_on_submit():
        user = User.query.filter_by(username=formLogIn.name.data).first()
        if user and user.check_password(password=formLogIn.password.data):
            login_user(user)
            return redirect(url_for('home_coctail.home'))
        flash('Invalid username/password combination')
    return render_template("mission.html", form1=formLogIn)

@app.route("/contact", methods=("GET", "POST"))
def contact():
    formLogIn = LogInForm()
    if formLogIn.validate_on_submit():
        user = User.query.filter_by(username=formLogIn.name.data).first()
        if user and user.check_password(password=formLogIn.password.data):
            login_user(user)
            return redirect(url_for('home_coctail.home'))
        flash('Invalid username/password combination')
    return render_template("contact.html", form1=formLogIn)

@app.route("/signup", methods=("GET", "POST"))
def signUp():
    formSignUp = SignupForm()
    formLogIn = LogInForm()
    print(formSignUp.validate())
    if formSignUp.validate_on_submit():
        #if formSignUp.login_bt.data:
        existing_user = User.query.filter_by(email=formSignUp.email.data).first()
        if existing_user is None:
            user = User(
                username=formSignUp.name.data,
                email=formSignUp.email.data,
                age=formSignUp.age.data,
                coctailNum=formSignUp.coctailNum.data
            )
            user.set_password(formSignUp.password.data)
            db.session.add(user)
            db.session.commit()         #create new user
            login_user(user)
            return redirect(url_for('home_coctail.home'))
        flash('Usuario ya existe con ese correo')     
    return render_template(
            "signUp.html",
            form2= formSignUp, 
            form1=formLogIn)

@app.route("/logout")
@login_required
def logout():
    """User logout"""
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('login'))