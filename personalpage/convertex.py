import os

from flask import render_template

from personalpage import app


## Data loading

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
CTEX_DATA = CURRENT_DIR + '/cthash/'

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