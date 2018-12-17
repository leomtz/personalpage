
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

## Routing    

@app.route("/")
def personal():
    return personal_page("lion")

@app.route("/notfound")
def notfound():
    return personal_page("notfound")

@app.route("/gtt")
def gttmap():
    return render_template("gtt.html")

@app.route("/cony")
def cony():
    return render_template("cony.html")

@app.route("/cony2017")
def cony2017():
    return render_template("cony2017.html")

@app.route("/cony2018")
def cony2018():
    return render_template("cony2018.html")

# Convertex

@app.route("/ct")
def convertex():
    f = open(CTEX_DATA + "default", "r", encoding="utf-8")
    content=f.read()
    f.close()
    return render_template("ct.html",link=False,content=content)

@app.route("/ct/<hash>")
def convertexlink(hash):
    try:
        f=open(CTEX_DATA + str(hash),"r",encoding="utf-8")
        content=f.read()
        f.close()
    except (OSError,IOError):
        content="OH NO! This is not a valid TeX-card link. But you can create a card to share with your friends or colleagues!"
    return render_template("ct.html",link=True,content=content)

# Spanish Convertex

@app.route("/es/ct")
def convertexes():
    f = open(CTEX_DATA + "default-es", "r", encoding="utf-8")
    content = f.read()
    f.close()
    return render_template("ct-es.html", link=False, content=content)

@app.route("/es/ct/<hash>")
def convertexlinkes(hash):
    try:
        f = open(CTEX_DATA + str(hash), "r", encoding="utf-8")
        content = f.read()
        f.close()
    except (OSError, IOError):
        content = u"OH NO! Esta no es una dirección de TeX-card válida. ¡Pero puedes crear una tarjeta para compartir con colegas y amigos!"
    return render_template("ct-es.html", link=True, content=content)

# Convertex Saving

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

# Personal Page

@app.route("/<section>")
def personal_page(section):
    if section in ["convertex"]:
        return convertex()
    rcontent=request(section)
    return render_template("personal.html", rcontent=rcontent)

@app.route("/request/")
def blankrequest():
    return redirect("/")

@app.route("/request/<section>")
def request(section):
    template=template_chooser(section)
    if section in ["about","links","lion"]:
        return render_template(template)
    if section in DATA_SECTIONS:
        items_array = CV.fetch_by_section_name(section)
        title=DATA_SECTIONS[section].title
        return render_template(template, items=items_array, title=title)
    else:
        return render_template("notfound.html")

# @app.route("/user/<username>")
# def show_profile(username):
#     username=username.title()
#     return render_template('user_page.html',user=username)
