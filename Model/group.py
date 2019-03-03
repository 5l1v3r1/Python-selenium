class Group:
    def __init__(app, name=None, header=None, footer=None, id=None):
        app.name = name
        app.header = header
        app.footer = footer
        app.id = id


    def __repr__(self):
        return "%s: %s" % (self.id, self.name)


    def __eq__(self, other):
        return self.id == other.id and self.name == other.name