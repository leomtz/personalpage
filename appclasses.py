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

class Job:
    def __init__(self, position, period, employer, description):
        self.position=position
        self.period=period
        self.employer=employer
        self.description=description