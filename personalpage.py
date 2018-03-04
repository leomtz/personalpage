
### IMPORTS ###
# Necessary Flask imports
from flask import Flask, url_for,render_template,request,redirect
# openpyxl helps to work with MSExcel databases
import os
import sys

# Tools to work with curriculum vitaes
import cvutils

### FLASK APP STARTS HERE $$$
app = Flask(__name__)

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)

## Data loading

CV=cvutils.cv_from_xlsx(CURRENT_DIR + '/data/CV.xlsx')
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

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

@app.route("/<section>")
def personal_page(section):
    rcontent=request(section)
    return render_template("personal.html", rcontent=rcontent)

@app.route("/request/")
def blankrequest():
    return redirect("/")

@app.route("/request/<section>")
def request(section):
    template=template_chooser(section)
    if section in ["about","links","lion", "convertex"]:
        return render_template(template)
    if section in DATA_SECTIONS:
        items_array = CV.fetch_by_section_name(section)
        title=DATA_SECTIONS[section].title
        return render_template(template, items=items_array, title=title)
    else:
        return render_template("notfound.html")


@app.route("/user/<username>")
def show_profile(username):
    username=username.title()
    return render_template('user_page.html',user=username)
