from flask import Flask
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/cv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import personalpage.models
import personalpage.cv
import personalpage.convertex
import personalpage.minipages

if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))