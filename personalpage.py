
### IMPORTS ###
# Necessary Flask imports
from flask import Flask, url_for,render_template,redirect
from flask import request as request_obj
# openpyxl helps to work with MSExcel databases
import os
import sys
import hashlib

# Tools to work with curriculum vitaes
import cvutils

### FLASK APP STARTS HERE $$$
app = Flask(__name__)

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)

## Data loading

CV=cvutils.cv_from_xlsx(CURRENT_DIR + '/data/CV.xlsx')
CTEX_DATA = CURRENT_DIR + '/cthash/'
DATA_SECTIONS=CV.sections

## Template setting

def template_chooser(section):
    if section in ['webp', 'pythonp', 'datascp']:
        return "coding_port.html"
    else:
        return section+".html"

#####################################
# Routing    
#####################################

#####################################

# Standard

@app.route("/")
def personal():
    return about()

@app.route("/notfound")
def notfound():
    return render_template("personalpage/notfound.html")

#####################################

# Convertex

## English Convertex

@app.route("/ct")
def convertex():
    f = open(CTEX_DATA + "default", "r", encoding="utf-8")
    content=f.read()
    f.close()
    return render_template("convertex/ct.html",link=False,content=content)

@app.route("/ct/<hash>")
def convertexlink(hash):
    try:
        f=open(CTEX_DATA + str(hash),"r",encoding="utf-8")
        content=f.read()
        f.close()
    except (OSError,IOError):
        content="OH NO! This is not a valid TeX-card link. But you can create a card to share with your friends or colleagues!"
    return render_template("convertex/ct.html",link=True,content=content)

## Spanish Convertex

@app.route("/es/ct")
def convertexes():
    f = open(CTEX_DATA + "default-es", "r", encoding="utf-8")
    content = f.read()
    f.close()
    return render_template("convertex/ct-es.html", link=False, content=content)

@app.route("/es/ct/<hash>")
def convertexlinkes(hash):
    try:
        f = open(CTEX_DATA + str(hash), "r", encoding="utf-8")
        content = f.read()
        f.close()
    except (OSError, IOError):
        content = u"OH NO! Esta no es una dirección de TeX-card válida. ¡Pero puedes crear una tarjeta para compartir con colegas y amigos!"
    return render_template("convertex/ct-es.html", link=True, content=content)

## Convertex Saving

@app.route("/cts", methods=['POST'])
def pconvertex():
    content=request_obj.form["content"]
    if len(content)>2250:
        return "Bad request: Text too long",400 
    hash = hashlib.sha1(content.encode("UTF-8")).hexdigest()
    filename = hash[0:5]
    f = open(CTEX_DATA + filename, "w", encoding="utf-8")
    content=f.write(content)
    f.close()
    lang='/'
    if "es" in request_obj.form["path"]:
        lang+="es/"
    return lang + "ct/" + filename

#####################################

# Personal Page

## About

@app.route("/about")
def about():
    education = reversed(CV.fetch_by_section_name("education"))
    jobs = reversed(CV.fetch_by_section_name("jobs"))
    awards = reversed(CV.fetch_by_section_name("awards"))
    return render_template("personalpage/about.html", education = education, jobs = jobs, awards = awards)

## Research

@app.route("/papers")
def papers():
    papers = list(reversed(CV.fetch_by_section_name("papers")))
    return render_template("personalpage/papers.html", papers = papers)

@app.route("/tresearch")
def tresearch():
    presentations = list(reversed(CV.fetch_by_section_name("presentations")))
    return render_template("personalpage/tresearch.html", presentations = presentations)

@app.route("/sresearch")
def sresearch():
    service = list(reversed(CV.fetch_by_section_name("service")))
    return render_template("personalpage/sresearch.html", service = service)

## Teaching

@app.route("/courses")
def courses():
    courseslist = list(reversed(CV.fetch_by_section_name("courses")))
    return render_template("personalpage/courses.html", courses = courseslist)

@app.route("/students")
def students():
    service = list(reversed(CV.fetch_by_section_name("service")))
    return render_template("personalpage/students.html", service = service)

@app.route("/steaching")
def steaching():
    service = list(reversed(CV.fetch_by_section_name("service")))
    return render_template("personalpage/steaching.html", service=service)

## Promotion

@app.route("/contests")
def contests():
    contests = list(reversed(CV.fetch_by_section_name("olympiad")))
    return render_template("personalpage/contests.html", contests = contests)

@app.route("/events")
def events():
    fairs = list(reversed(CV.fetch_by_section_name("fairs")))
    return render_template("personalpage/events.html", fairs = fairs)

@app.route("/writings")
def writings():
    papers = list(reversed(CV.fetch_by_section_name("prompub")))
    media = list(reversed(CV.fetch_by_section_name("media")))
    return render_template("personalpage/writings.html", papers = papers, media=media)

@app.route("/tpromotion")
def tpromotion():
    presentations = list(reversed(CV.fetch_by_section_name("presentations")))
    return render_template("personalpage/tpromotion.html", presentations = presentations)

## Coding

@app.route("/coding")
def coding():
    codinglist = list(reversed(CV.fetch_by_section_name("wholep")))
    return render_template("personalpage/coding.html", coding = codinglist)

#####################################

# MiniPages

## Polynomials 2019
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

#####################################

# # Old Requests
# @app.route("/request/<section>")
# def request(section):
#     template=template_chooser(section)
#     if section in ["about","links","lion"]:
#         return render_template(template)
#     if section in DATA_SECTIONS:
#         items_array = CV.fetch_by_section_name(section)
#         title=DATA_SECTIONS[section].title
#         return render_template(template, items=items_array, title=title)
#     else:
#         return render_template("notfound.html")

# @app.route("/request/")
# def blankrequest():
#     return redirect("/")

# @app.route("/<section>")
# def personal_page(section):
#     if section in ["convertex"]:
#         return convertex()
#     rcontent=request(section)
#     return render_template("personal.html", rcontent=rcontent)