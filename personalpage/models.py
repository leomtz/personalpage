from personalpage import app
from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    name_spa = db.Column(db.String(80), unique=True, nullable=False)


class Institution(db.Model):
    __tablename__ = 'institution'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    name_spa = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Institution %r>' % self.name

class Award(db.Model):
    __tablename__ = 'award'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    title_spa = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date(), nullable=False,
        default=date.today())
    description = db.Column(db.String(200), nullable=False)
    description_spa = db.Column(db.String(200), nullable=False)
    institution = db.Column(db.Integer, db.ForeignKey('institution.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Award %r>' % self.title

class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    title_spa = db.Column(db.String(80), unique=True, nullable=False)
    start_date = db.Column(db.Date(), nullable=False,
        default=date.today())
    end_date = db.Column(db.Date(), default=date.today())
    description = db.Column(db.String(140), nullable=False)
    description_spa = db.Column(db.String(140), nullable=False)
    institution = db.Column(db.Integer, db.ForeignKey('institution.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Education %r>' % self.title

class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    title_spa = db.Column(db.String(80), unique=True, nullable=False)
    start_date = db.Column(db.Date(), nullable=False,
        default=date.today())
    end_date = db.Column(db.Date(), default=date.today())
    description = db.Column(db.String(140), nullable=False)
    description_spa = db.Column(db.String(140), nullable=False)
    institution = db.Column(db.Integer, db.ForeignKey('institution.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Job %r>' % self.title

class Contest(db.Model):
    __tablename__ = 'contest'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    title_spa = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(140), nullable=False)
    description_spa = db.Column(db.String(140), nullable=False)
    audience = db.Column(db.String(80), nullable=False)
    audience_spa = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Contest %r>' % self.title

class RoleContest(db.Model):
    __tablename__ = 'rolecontest'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    name_spa = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(140), nullable=False)
    description_spa = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return '<ContestRole %r>' % self.title

class ContestRoleAssign(db.Model):
    __tablename__ = 'contestroleassign'
    id = db.Column(db.Integer, primary_key=True)
    contest_id = db.Column(db.Integer, db.ForeignKey('contest.id'))
    role_contest_id = db.Column(db.Integer, db.ForeignKey('rolecontest.id'))
    start_date = db.Column(db.Date(), default=date.today())
    end_date = db.Column(db.Date(), default=date.today())

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date(), nullable=False,
        default=date.today())
    end_date = db.Column(db.Date(),
        default=date.today())
    sem_unam = db.Column(db.String(20), unique=True, nullable=False)

    role = db.Column(db.String(20), unique=True, nullable=False)
    role_spa = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    title_spa = db.Column(db.String(80), unique=True, nullable=False)
    course_type = db.Column(db.String(20), unique=True, nullable=False)

    institution = db.Column(db.Integer, db.ForeignKey('institution.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Course %r>' % self.title

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date(), default=date.today())
    
    description = db.Column(db.String(140), nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    service_type = db.Column(db.String(20), nullable=False)

    institution = db.Column(db.Integer, db.ForeignKey('institution.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Service %r>' % self.title

class Awareness(db.Model):
    __tablename__ = 'awareness'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), default=date.today())

    title = db.Column(db.String(80), unique=True, nullable=False)
    title_spa = db.Column(db.String(80), unique=True, nullable=False)
    
    description = db.Column(db.String(140), nullable=False)
    description_spa = db.Column(db.String(140), nullable=False)
    
    audience = db.Column(db.String(80), nullable=False)
    audience_spa = db.Column(db.String(80), nullable=False)

    institution = db.Column(db.Integer, db.ForeignKey('institution.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Awareness %r>' % self.title

class Talk(db.Model):
    __tablename__ = 'talk'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), default=date.today())

    title = db.Column(db.String(80), unique=True, nullable=False)

    slides = db.Column(db.String(140))
    
    event = db.Column(db.String(140), nullable=False)
    event_type =  db.Column(db.String(80), nullable=False)
    event_type_spa = db.Column(db.String(80), nullable=False)

    institution = db.Column(db.Integer, db.ForeignKey('institution.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return '<Talk %r>' % self.title

class CodingItem(db.Model):
    __tablename__ = 'codingitem'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date(), default=date.today())
    end_date = db.Column(db.Date(), default=date.today())

    title = db.Column(db.String(80), unique=True, nullable=False)
    title_spa = db.Column(db.String(80), unique=True, nullable=False)
    
    description = db.Column(db.String(140), nullable=False)
    description_spa = db.Column(db.String(140), nullable=False)
    
    main_tag = db.Column(db.String(80), nullable=False)
    technologies = db.Column(db.String(140))

    link = db.Column(db.String(140))
    github = db.Column(db.String(140))

    def __repr__(self):
        return '<CodingItem %r>' % self.title

class MainstreamMedia(db.Model):
    __tablename__ = 'mainstreammedia'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), default=date.today())

    title = db.Column(db.String(80), unique=True, nullable=False)
    media_name = db.Column(db.String(80), nullable=False)
    media_type = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<MainstreamMedia %r>' % self.title

class ScientificPublication(db.Model):
    __tablename__ = 'scientificpublication'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), default=date.today())
    title = db.Column(db.String(140), nullable=False)

    publication_type = db.Column(db.String(80), nullable=False)
    publication_status = db.Column(db.String(80), nullable=False)

    authors = db.Column(db.String(300), nullable=False)
    publisher = db.Column(db.String(80))
    journal = db.Column(db.String(80))
    volume = db.Column(db.String(80))
    pages = db.Column(db.String(80))
    
    doi = db.Column(db.String(80))
    arxiv = db.Column(db.String(80))
    link = db.Column(db.String(80))

    def __repr__(self):
        return '<MainstreamMedia %r>' % self.title