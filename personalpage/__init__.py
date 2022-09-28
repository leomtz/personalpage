from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/cv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import personalpage.models
import personalpage.cv
import personalpage.convertex
import personalpage.minipages