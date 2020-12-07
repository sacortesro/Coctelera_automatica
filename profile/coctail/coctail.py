from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app as app
from flask_login import current_user, login_required

#from flask_mqtt import Mqtt
#mqtt = Mqtt(app)

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
    
    #print(ingrList)
    #ingrList1 = [ingrList[1].replace(' ', ''), ingrList[3].replace(' ', ''), ingrList[5].replace(' ', ''), ingrList[7].replace(' ', '')]
    #print(ingrList1)
    #ingrList2 = [ingrList1[0].replace('/', ''), ingrList1[1].replace('/', ''), ingrList1[2].replace('/', ''), ingrList1[3].replace('/', '')]
    #print(ingrList2)
    #ingrList3 = [ingrList2[0].replace('can', ''), ingrList2[1].replace('can', ''), ingrList2[2].replace('can', ''), ingrList2[3].replace('can', '')]
    #print(ingrList3)
    #ingrList4 = [ingrList3[0].replace('tsp', ''), ingrList3[1].replace('tsp', ''), ingrList3[2].replace('tsp', ''), ingrList3[3].replace('tsp', '')]
    #print(ingrList4)
    #ingrList5 = [ingrList4[0].replace('shot', ''), ingrList4[1].replace('shot', ''), ingrList4[2].replace('shot', ''), ingrList4[3].replace('shot', '')]
    #print(ingrList5)
    
    #ingrint = [1+int(ingrList5[0]),1+int(ingrList5[1]),1+int(ingrList5[2]),1+int(ingrList5[3])]
    #print(ingrint)
    #ingrmm = [ingrint[0]*8, ingrint[1]*8, ingrint[2]*8, ingrint[3]*8]
    #print(ingrmm)
    
    #mqtt.publish('server', 'Preparando Coctail')
    #mqtt.publish('ingr', 'a'+str(ingrmm[0])+'b'+str(ingrmm[1])+'c'+str(ingrmm[2])+'d'+str(ingrmm[3]))
    
    if form.validate_on_submit():
        return redirect(url_for('home_coctail.home'))
    return render_template("confirmCoctail.html",desCoc=jsonCoctail, ingrList=ingrList, form=form)
