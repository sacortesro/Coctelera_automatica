from flask import Blueprint, render_template
from flask import current_app as app

from .form_get_coctail import SearchForm
from .dataJSON import jsonSearch

# Blueprint Configuration
home_coctail = Blueprint(
    'home_coctail', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_coctail.route('/home', methods=["GET", "POST"])
def home():    
    form = SearchForm()
    if form.validate_on_submit():
        strSearch = form.coctail_search.data
    else:
        strSearch = "a"
        
    data = jsonSearch(strSearch)
    return render_template("home.html", form=form, data = data) 
