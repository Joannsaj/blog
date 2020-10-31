class Quote:
    def __init__(self, author, id, quote, permalink):
        self.author = author
        self.id = id 
        self.quote = quote
        self.permalink = permalink

class Blog:
    def __init__(self, text):
        self.text = text     