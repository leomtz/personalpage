import os
import sys
import hashlib

from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

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
    education = Education.query\
        .join(Institution)\
        .join(Location,Education.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    jobs = Job.query\
        .join(Institution)\
        .join(Location,Job.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    awards = Award.query\
        .join(Institution)\
        .join(Location, Award.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    return render_template("personalpage/about.html", education = education, jobs = jobs, awards = awards)

## Research

@app.route("/papers")
def papers():
    papers = ScientificPublication.query\
        .all()
    return render_template("personalpage/papers.html", papers = papers)

@app.route("/tresearch")
def tresearch():
    talks = Talk.query\
        .join(Institution)\
        .join(Location,Talk.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    return render_template("personalpage/tresearch.html", talks=talks)

@app.route("/sresearch")
def sresearch():
    r_journal = Service.query\
        .filter(Service.service_type=='r_journal')\
        .all()
    r_conference = Service.query\
        .filter(Service.service_type=='r_conference')\
        .all()
    service = Service.query\
        .filter(Service.service_type=="o_event_research")\
        .join(Institution)\
        .join(Location, Service.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    print(service)
    return render_template("personalpage/sresearch.html", r_journal=r_journal, r_conference=r_conference, service = service)

## Teaching

@app.route("/courses")
def courses():
    courseslist = list(reversed(CV.fetch_by_section_name("courses")))
    return render_template("personalpage/courses.html", courses = courseslist)

@app.route("/students")
def students():
    students = Service.query\
        .join(Institution)\
        .join(Location, Service.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .order_by(desc(Service.date))\
        .all()
    return render_template("personalpage/students.html", students = students)

@app.route("/steaching")
def steaching():
    service = Service.query\
        .join(Institution)\
        .join(Location, Service.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .order_by(desc(Service.date))\
        .all()
    return render_template("personalpage/steaching.html", service=service)

## Promotion

@app.route("/contests")
def contests():
    contests=ContestRoleAssign.query\
        .join(Contest)\
        .join(RoleContest)\
        .add_entity(Contest)\
        .add_entity(RoleContest)\
        .all()
    # contests = list(reversed(CV.fetch_by_section_name("olympiad")))
    return render_template("personalpage/contests.html", contests = contests)

@app.route("/events")
def events():
    fairs = list(reversed(CV.fetch_by_section_name("fairs")))
    return render_template("personalpage/events.html", fairs = fairs)

@app.route("/writings")
def writings():
    papers = ScientificPublication.query\
        .all()
    media = MainstreamMedia.query\
        .all()
    return render_template("personalpage/writings.html", papers = papers, media=media)

@app.route("/tpromotion")
def tpromotion():
    talks = Talk.query\
        .join(Institution)\
        .join(Location,Talk.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    print(talks)
    return render_template("personalpage/tpromotion.html", talks=talks)

## Coding

@app.route("/coding")
def coding():
    codinglist = list(reversed(CV.fetch_by_section_name("wholep")))
    return render_template("personalpage/coding.html", coding = codinglist)