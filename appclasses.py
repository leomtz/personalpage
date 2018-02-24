# Some classes related to CV information

class Paper:
    def __init__(self, kind, title, authors,
         journal, year, volume, pages, doi):
        self.kind= kind
        self.title=title
        self.authors=authors
        self.journal=journal
        self.year=year
        self.volume=volume
        self.pages=pages
        self.doi=doi

class Presentation:
    def __init__(self, kind, title, venue, conference,
         year, link):
        self.kind=kind
        self.title=title
        self.venue=venue
        self.conference=conference
        self.year=year
        self.link=link
        self.location=location

class Job:
    def __init__(self, position, period, employer, description):
        self.position=position
        self.period=period
        self.employer=employer
        self.description=description

class ArtItem:
    def __init__(self, kind, title, year, technique, link, description):
        self.kind=kind
        self.title=title
        self.year=year
        self.technique=technique
        self.description=description
        self.link=link

class ProgrammingItem:
    def __init__(self, title, year, technology, link, description):
        self.title=title
        self.year=year
        self.technology=technology
        self.description=description
        self.link=link