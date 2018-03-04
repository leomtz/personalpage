# class CVItem(object):
#     def __init__(self, *, id, title, date, description, links, tags):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.tags = tags

# class Certificate(CVItem):
#     name="Certificate"
#     def __init__(self, *, institution, location, **kwargs):
#         super().__init__(**kwargs)
#         self.institution = institution
#         self.location = location
#         self.date=2008

# d={"id":100, "title":"Casa", "date":2000, "description":"Grande y buena", "links":[1,2,4], "tags":[5,8]}
# e={"id":120, "title":"Casa", "date":2000, "description":"Grande y buena", "links":[1,2,4], "tags":[5,8]}
# item=CVItem(**d)
# certificate=Certificate2007(institution="UNAM", location="casa",**e)
# print(item.id)
# print(certificate.date)
# print(certificate.id)

class Persona():
    def __init__(self, name):
        self.name=name

    def da_nombre(self):
        print(self.name)

class Empleado(Persona):
    def __init__(self,name):
        super().__init__(name)

a=Empleado("Jorge")
a.da_nombre()