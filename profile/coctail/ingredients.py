from flask_wtf import FlaskForm
from wtforms import (SubmitField)
                     
                     
                     
                     
def ingredients(jsonCoctail):
    a=1
    ingList=[]       
    while jsonCoctail.get("drinks")[0].get("strIngredient"+str(a))!= None:
        ingList.append(jsonCoctail.get("drinks")[0].get("strIngredient"+str(a)))
        ingList.append(jsonCoctail.get("drinks")[0].get("strMeasure"+str(a)))
        a=a+1            
  
    return [ingList]
...

class confirmCoc(FlaskForm):
    submit=SubmitField('Confirmar orden')
            
