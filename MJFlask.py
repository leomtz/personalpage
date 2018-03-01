
### IMPORTS ###
# Necessary Flask imports
from flask import Flask, url_for,render_template,request,redirect
# openpyxl helps to work with MSExcel databases
import os
import sys

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)

# Local imports to work with CV
from cvutils_dev import *
cvu=__import__("cvutils_dev")

### FLASK APP STARTS HERE $$$

app = Flask(__name__)
CV_LOCATION= CURRENT_DIR + '/data/CV.xlsx'
SECTIONS_DB=openpyxl.load_workbook(CURRENT_DIR + '/data/Sections.xlsx')
sections_ws=SECTIONS_DB["SectionManager"]
subsections_ws=SECTIONS_DB["SubsectionManager"]
sections=[]
subsections=[]

def get_props(subsection):
    return list(filter(lambda ss: ss[1]==subsection, subsections))[0]

def get_filter(subsection):
    ss_props=list(filter(lambda ss: ss[1]==subsection, subsections))[0]
    tag_filter=None


# OLD CODE
#
# @app.route("/")
# def hello():
#     return render_template("home.html")
# @app.route("/math", methods=['POST', 'GET'])
# def math():
#     try:
#         coolmath=request.args['mathjax']
#     except:
#         coolmath="En esta página puedes poner código 
#                   $\LaTeX$ como $\\frac{1}{d+1}$."
#     return render_template('math.html',coolmath=coolmath)
# @app.route("/math2")
# def math2():
#     return render_template('math2.html')

@app.route("/")
def personal():
    return personal_page("home")

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

@app.route("/request/<subsection>")
def request(subsection):
    if subsection in SUBSECTIONS:
        if subsection=="home":
            return render_template("lion.html")
        if ss_props[3]=="True":
            cv=fetch_CV(CV_LOCATION)
            # get handling class
            # get handling template
            # get title
            handling_class=
            if ss_props[5] is not None:
                tag_filter=ss_props[5].split(", ")
            if subsection in ["datascp","pythonp","webp"]:
                return render_template("portfolio_tag.html", filter_title=ss_props[3])
            items_array=fetch_from_CV(cv,getattr(cvu,ss_props[4]) ,tag_filter)
            return render_template(subsection+".html",items=items_array)
        return render_template(subsection+".html")
    else:
        return render_template("notfound.html")


@app.route("/user/<username>")
def show_profile(username):
    username=username.title()
    return render_template('user_page.html',user=username)