from flask import render_template

from personalpage import app

####################################

# MiniPages

## Polytopes 2019
@app.route("/poly2019/")
def polytopes():
    return render_template("minipages/hdrarnau.html")

## Descartes 2020
@app.route("/descartes/")
def descartes():
    return render_template("minipages/descartes.html")

## SMCCGDC 2021
@app.route("/smccgdc/")
def smcc():
    return render_template("minipages/smcc.html")

## GTT Diagram

@app.route("/gtt")
def gttmap():
    return render_template("minipages/gtt.html")

## Sobrinos Tía Cony

@app.route("/cony")
def cony():
    return render_template("cony/cony.html")

@app.route("/cony<year>")
def conyyear(year): 
    if year in ["2015","2016","2017","2018"]:
        return render_template("cony/cony{}.html".format(year))
    else:
        return render_template("notfound.html")