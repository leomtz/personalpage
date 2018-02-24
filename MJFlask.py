
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
from appclasses import Job, Paper

### FUNCTIONS ###
# Some functions for dealing with data from xls databases with curriculum info

def fetch_papers():
    papers_DB = openpyxl.load_workbook(
        r'data\Publications.xlsx',
        data_only=True
        )
    papers = papers_DB['Papers']
    papers_array = []
    j=3
    # for j in range(3,10):
    while papers.cell(row=j,column=1).value is not None:
        new_paper=Paper(
            *[papers.cell(row=j,column=k).value for k in range(2,10)]
            )
        papers_array+=[new_paper]
        j+=1
    return papers_array

### FLASK APP STARTS HERE $$$

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("home.html")

# @app.route("/math", methods=['POST', 'GET'])
# def math():
#     try:
#         coolmath=request.args['mathjax']
#     except:
#         coolmath="En esta página puedes poner código $\LaTeX$ como $\\frac{1}{d+1}$."
#     return render_template('math.html',coolmath=coolmath)

# @app.route("/math2")
# def math2():
#     return render_template('math2.html')

@app.route("/")
def personal():
    return personal_page("home")

@app.route("/<section>")
def personal_page(section):
    rcontent=request_section(section)
    print(type(rcontent))
    return render_template("personal.html", rcontent=rcontent)

@app.route("/request/<section>")
def request_section(section):
    if section=="home":
        return render_template("lion.html")
    if section=="papers":
        papers_array=fetch_papers()
        return render_template("papers.html",papers_array=papers_array)
    return render_template("%s.html" % section)

@app.route("/user/<username>")
def show_profile(username):
    username=username.title()
    return render_template('user_page.html',user=username)