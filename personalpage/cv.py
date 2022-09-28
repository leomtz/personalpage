import os
import sys
import hashlib

from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# Tools to work with curriculum vitaes
from personalpage import app
import personalpage.cvutils as cvutils
from personalpage.models import *

### FLASK APP STARTS HERE $$$
# app = Flask(__name__)

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)

CV=cvutils.primaryclasses.cv_from_xlsx(CURRENT_DIR + '/data/CV.xlsx')
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

# Personal Page

## About

@app.route("/about")
def about():
    education = Education.query.join(Institution).join(Location,Education.location==Location.id).add_entity(Institution).add_entity(Location).all()
    jobs = Job.query.join(Institution).join(Location,Job.location==Location.id).add_entity(Institution).add_entity(Location).all()
    awards = Award.query.join(Institution).join(Location, Award.location==Location.id).add_entity(Institution).add_entity(Location).all()
    return render_template("personalpage/about.html", education = education, jobs = jobs, awards = awards)

## Research

@app.route("/papers")
def papers():
    papers = list(reversed(CV.fetch_by_section_name("papers")))
    return render_template("personalpage/papers.html", papers = papers)

@app.route("/tresearch")
def tresearch():
    talks = Talk.query.join(Institution).join(Location,Talk.location==Location.id).add_entity(Institution).add_entity(Location).all()
    return render_template("personalpage/tresearch.html", talks=talks)

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
    talks = Talk.query.join(Institution).join(Location,Talk.location==Location.id).add_entity(Institution).add_entity(Location).all()
    return render_template("personalpage/tresearch.html", talks=talks)

## Coding

@app.route("/coding")
def coding():
    codinglist = list(reversed(CV.fetch_by_section_name("wholep")))
    return render_template("personalpage/coding.html", coding = codinglist)