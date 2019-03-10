from sys import maxsize

class Group:
    def __init__(app, name=None, header=None, footer=None, id=None):
        app.name = name
        app.header = header
        app.footer = footer
        app.id = id


    def __repr__(self):
        return "%s:%s:%s:%s:" % (self.id, self.name, self.header, self.footer)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name


    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize