from flask import Blueprint, render_template, request
from flask import current_app as app

from .jsonDesc import fjsonDesc
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