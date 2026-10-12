class Post:
    def __init__(self, author, title, caption, message):
            self.author = author
            self.title = title
            self.caption = caption
            self.message = message

    def to_dict(self):
        return { "author": self.author, "title": self.title, "caption": self.caption, "message": self.message}

    
    