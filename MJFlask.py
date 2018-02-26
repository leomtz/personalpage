
### IMPORTS ###
# Necessary Flask imports
from flask import Flask, url_for,render_template,request,redirect
# openpyxl helps to work with MSExcel databases
import openpyxl

# Local imports to work with CV
from cvutils import Job, Paper, Award, ProgrammingItem, Presentation
from cvutils import fetch_CV, fetch_from_CV

### FLASK APP STARTS HERE $$$

app = Flask(__name__)
CV_LOCATION=r'data\CV.xlsx'

SECTIONS=["papers", "jobs", "awards", "drawings", "education",
            "home", "links", "lion", "music", "olympiad", "papers",
            "pythonp", "presentations", "teaching", "webp", "about",
            "notfound","datascp", "wholep", "service","fairs",
            "prompub", "media", "stories", "random"
            ] 

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
    print(type(rcontent))
    return render_template("personal.html", rcontent=rcontent)

@app.route("/request/")
def blankrequest():
    return redirect("/")

@app.route("/request/<section>")
def request(section):
    fetch_classes={"papers":Paper, "jobs":Job, "awards":Award, 
        "wholep":ProgrammingItem, "pythonp":ProgrammingItem,
        "datascp":ProgrammingItem, "webp":ProgrammingItem,
        "presentations": Presentation
        }
    if section in SECTIONS:
        if section=="home":
            return render_template("lion.html")
        if section in fetch_classes:
            cv=fetch_CV(CV_LOCATION)
            items_array=fetch_from_CV(cv,fetch_classes[section])
            return render_template(section+".html",items=items_array)
        return render_template(section+".html")
    else:
        return render_template("notfound.html")

@app.route("/user/<username>")
def show_profile(username):
    username=username.title()
    return render_template('user_page.html',user=username)