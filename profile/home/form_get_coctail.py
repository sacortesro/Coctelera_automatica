from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField)                    
# from wtforms.validators import (Email,
#                                 EqualTo,
#                                 Length)

class SearchForm(FlaskForm):
    coctail_search = StringField('searchText')
    searchButton = SubmitField('Search')

...