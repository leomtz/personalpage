# SUPORTED CLASSES
# CVItem
# -- Certificate
# ---- Award
# ---- Education
# ---- Job
# -- Event
# ---- Contest
# ---- Course
# ---- Talk
# ---- ScienceFair
# ---- Service
# -- PortfolioItem
# ---- ArtItem
# ---- CodingItem
# -- Publication
# ---- Book
# ---- MainstreamMedia
# ---- ScientificPublication
### Fundamental classes for the module

class CVItem(object):
    # The basic CV item. You did something explainable sometime, and you
    # want to give tags to it for further classification. In order to add
    # reference to media, we also manage Links, exterior world references
    # to the item that help to verify/check/consult it.
    #
    # It can be extended to give it further properties. Check itemclasses.py.
    def __init__(self, *, id, title, date, description, links, tags):
        self.id = id
        self.title = title
        self.date = date
        self.description = description
        self.links = links
        if type(tags) is str:
            self.tags = tags.split(", ")
        else:
            self.tags = tags
        if self.tags == None:
            self.tags_set = set()
        else:
            self.tags_set = set(self.tags)

    def properties(self):
        # Will return a list of all the callable properties of the object.
        pass

# Level 1 Items

class Certificate(CVItem):
    def __init__(self, *, institution, location, **kwargs):
        super().__init__(**kwargs)
        self.institution = institution
        self.location = location


class Event(CVItem):
    def __init__(self, *, location, role, **kwargs):
        super().__init__(**kwargs)
        self.location = location
        self.role = role


class PortfolioItem(CVItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Publication(CVItem):
    def __init__(self, *, authors, publisher, **kwargs):
        super().__init__(**kwargs)
        self.authors = authors
        self.publisher = publisher

# Level 2 Items


class Award(Certificate):
    sheet = "Award"

    def __init__(self, **kwargs):
        super().__init__(links=None, **kwargs)


class Education(Certificate):
    sheet = "Education"

    def __init__(self, *, start_date, end_date, **kwargs):
        super().__init__(date=[start_date, end_date], links=None, **kwargs)


class Job(Certificate):
    sheet = "Job"

    def __init__(self, *, start_date, end_date, **kwargs):
        super().__init__(date=[start_date, end_date], links=None, **kwargs)


class Contest(Event):
    sheet = "Contest"

    def __init__(self, *, start_date, end_date, audience, **kwargs):
        super().__init__(links=None, date=[start_date, end_date], **kwargs)
        self.audience = audience


class Course(Event):
    sheet = "Course"

    def __init__(self, *, institution, **kwargs):
        super().__init__(description="", links=None, **kwargs)
        self.institution = institution


class Talk(Event):
    sheet = "Talk"

    def __init__(self, *, audience, institution, file, **kwargs):
        super().__init__(role="lecturer", links={"file": file}, **kwargs)
        self.audience = audience
        self.institution = institution


class ScienceFair(Event):
    sheet = "ScienceFair"

    def __init__(self, *, audience, institution, **kwargs):
        super().__init__(links=None, **kwargs)
        self.audience = audience
        self.institution = institution


class Service(Event):
    sheet = "Service"

    def __init__(self, *, institution, **kwargs):
        super().__init__(links=None, **kwargs)
        self.institution = institution


class ArtItem(PortfolioItem):
    sheet = "ArtItem"

    def __init__(self, *, technique, youtube, file, **kwargs):
        super().__init__(links={"file": file, "youtube": youtube}, **kwargs)
        self.technique = technique


class CodingItem(PortfolioItem):
    sheet = "CodingItem"

    def __init__(self, *, technologies, github, web, **kwargs):
        super().__init__(links={"github": github, "web": web}, **kwargs)
        self.technologies = technologies


class Book(Publication):
    sheet = "Book"

    def __init__(self, *, file, **kwargs):
        super().__init__(links={"file": file}, **kwargs)


class MainstreamMedia(Publication):
    sheet = "MainstreamMedia"

    def __init__(self, *, media_name, media_type, file, **kwargs):
        super().__init__(links={"file": file}, **kwargs)
        self.media_name = media_name
        self.media_type = media_type


class ScientificPublication(Publication):
    sheet = "ScientificPublication"

    def __init__(self, *, journal, volume, pages, doi, arxiv, web, **kwargs):
        super().__init__(links={"arxiv": arxiv,
                                "doi": doi, "web": web}, **kwargs)
        self.journal = journal
        self.volume = volume
        self.pages = pages
