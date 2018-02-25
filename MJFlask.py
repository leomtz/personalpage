
### IMPORTS ###
# Necessary Flask imports
from flask import Flask, url_for,render_template,request

# openpyxl helps to work with MSExcel databases
import openpyxl

# Local imports to work with CV
from cvutils import Job, Paper, Award
from cvutils import fetch_CV, fetch_from_CV

### FLASK APP STARTS HERE $$$

app = Flask(__name__)
CV_LOCATION=r'data\CV.xlsx'

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

@app.route("/<section>")
def personal_page(section):
    rcontent=request(section)
    print(type(rcontent))
    return render_template("personal.html", rcontent=rcontent)

@app.route("/request/<section>")
def request(section):
    fetch_classes={"papers":Paper, "jobs":Job, "awards":Award}
    if section=="home":
        return render_template("lion.html")
    if section in fetch_classes:
        CV=fetch_CV(CV_LOCATION)
        items_array=fetch_from_CV(CV,fetch_classes[section])
        return render_template(section+".html",items=items_array)
    return render_template("%s.html" % section)

@app.route("/user/<username>")
def show_profile(username):
    username=username.title()
    return render_template('user_page.html',user=username)