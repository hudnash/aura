class Book:
    def __init__(self):
        pass
    @version.setter
    def add_version(self,text):
        pass
class Version(Book):
    def __init__(self):
        pass
    @pages.setter
    def get_pages(self):
        pass
class Page(Version):
    def __init__(self):
        pass
    @sentence.setter
    def get_sentences(self,text):
        pass
class Sentence(Page):
    def __init__(self):
        pass
    @id.setter
    def id(self):
        pass # This will be a number telling us which sentence it is in the text. May be used for cross-referencing.