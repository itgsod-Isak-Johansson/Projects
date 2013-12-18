

class Tidning():
    def __init__(self):
        self.title = "dn"
        self.number_of_articles = 3
        self.number_of_pages = 100000000000



    def get_property(self):
        return self.title

    def set_property(self,value):
        self.titlee = value
        return self.title



def main():
    obj = Tidning()
    print obj.get_property()
    obj.get_property("Svd")


main()