from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app as app
from flask_login import current_user, login_required


from .jsonDesc import fjsonDesc
from .ingredients import ingredients, confirmCoc
# Blueprint Configuration
coctail_bp = Blueprint(
    'coctail_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@coctail_bp.route('/coctail' , methods=["GET","POST"])
def desCoctail():
    idCoctail=request.args.get('type')
    jsonCoctail=fjsonDesc(idCoctail)
    return render_template("desc.html",desCoc=jsonCoctail)

@coctail_bp.route('/coctail/order' , methods=["GET"])
@login_required
def orderCoctail():
    form=confirmCoc()
    idCoctail=request.args.get('type')
    jsonCoctail=fjsonDesc(idCoctail) 
    ingrList=ingredients(jsonCoctail)[0]
    if form.validate_on_submit():
        return redirect(url_for('home_coctail.home'))
    return render_template("confirmCoctail.html",desCoc=jsonCoctail, ingrList=ingrList, form=form)