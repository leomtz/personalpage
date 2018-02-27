
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

# Fetch sections. Probably want it as part os cvutils module
y = 3
while sections_ws.cell(row=y,column=1).value is not None:
    new_section=[sections_ws.cell(row=y,column=x).value for x in range(1,5)]
    sections+=[new_section]
    y+=1

# Fetch subsections. Probably want it as part os cvutils module
y=3
while subsections_ws.cell(row=y,column=1).value is not None:
    new_subsection=[subsections_ws.cell(row=y,column=x).value for x in range(1,7)]
    subsections+=[new_subsection]
    y+=1

SUBSECTIONS=[s[1] for s in subsections]
TITLES_SS=[s[2] for s in subsections]
FETCH_SS=[s[3] for s in subsections]
CLASS_SS=[s[4] for s in subsections]
TAGS_SS=[s[5] for s in subsections]

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
        ss_props=list(filter(lambda ss: ss[1]==subsection, subsections))[0]
        if subsection=="home":
            return render_template("lion.html")
        if ss_props[3]=="True":
            cv=fetch_CV(CV_LOCATION)
            tag_filter=None
            if ss_props[5] is not None:
                tag_filter=ss_props[5].split(", ")
            items_array=fetch_from_CV(cv,getattr(cvu,ss_props[4]) ,tag_filter)
            return render_template(subsection+".html",items=items_array)
        return render_template(subsection+".html")
    else:
        return render_template("notfound.html")


@app.route("/user/<username>")
def show_profile(username):
    username=username.title()
    return render_template('user_page.html',user=username)