
### IMPORTS ###
# Necessary Flask imports
from flask import Flask, url_for,render_template,request

# openpyxl helps to work with MSExcel databases
import openpyxl
from shutil import copyfile
# We may need the following for statistics
import numpy as np
import matplotlib.pyplot as plt

# Local imports
from appclasses import Job, Paper, Award

### FUNCTIONS ###
# Functions to load the items from the CV

def fetch_CV():
    return openpyxl.load_workbook(r'data\CV.xlsx', data_only=True)

def fetch_from_CV(section,class_):
    CV = fetch_CV()
    data_ws = CV[section.title()]
    item_array = []
    num_attr = class_.num_attr
    j = 3 #Compensate for DB column titles
    while data_ws.cell(row=j,column=1).value is not None:
        new_item=class_(
            *[data_ws.cell(row=j,column=k).value for k in range(2,2+num_attr)]
            )
        item_array+=[new_item]
        j+=1
    return item_array

### FLASK APP STARTS HERE $$$

app = Flask(__name__)

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
        items_array=fetch_from_CV(section,fetch_classes[section])
        return render_template(section+".html",items=items_array)
    return render_template("%s.html" % section)

@app.route("/user/<username>")
def show_profile(username):
    username=username.title()
    return render_template('user_page.html',user=username)