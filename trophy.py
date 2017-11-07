
class trophy:
    def __init__(self, title="", desc="", date="", typ="", imgurl=""):
        self.title = title
        self.desc = desc
        self.date = date
        self.typ = typ
        self.imgurl = imgurl

    def print(self):
        print(self.title)
        print("\t" + self.desc)
        print("\t" + self.date)
        print("\t" + self.typ)
        print("\t" + self.imgurl)
