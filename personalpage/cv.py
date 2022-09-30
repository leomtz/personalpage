from flask import render_template
from sqlalchemy import desc

from personalpage import app
from personalpage.models import *

#####################################
# Routing    
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
        .select_from(Education)\
        .join(Institution)\
        .join(Location,Education.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    jobs = Job.query\
        .select_from(Job)\
        .join(Institution)\
        .join(Location,Job.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    awards = Award.query\
        .select_from(Award)\
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
        .select_from(Talk)\
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
        .select_from(Service)\
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
    courses = Course.query\
        .select_from(Course)\
        .join(Institution)\
        .join(Location, Course.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    return render_template("personalpage/courses.html", courses = courses)

@app.route("/students")
def students():
    students = Service.query\
        .select_from(Service)\
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
        .select_from(Service)\
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
    return render_template("personalpage/contests.html", contests = contests)

@app.route("/events")
def events():
    events=Awareness.query\
        .select_from(Awareness)\
        .join(Institution)\
        .join(Location, Awareness.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    print(events)
    return render_template("personalpage/events.html", events = events)

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
        .select_from(Talk)\
        .join(Institution)\
        .join(Location,Talk.location==Location.id)\
        .add_entity(Institution)\
        .add_entity(Location)\
        .all()
    return render_template("personalpage/tpromotion.html", talks=talks)

## Coding

@app.route("/coding")
def coding():
    coding_list = CodingItem.query\
        .all()
    return render_template("personalpage/coding.html", coding_list = coding_list)