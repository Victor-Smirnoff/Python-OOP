import sys


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


print(Book(*list(map(str.strip, sys.stdin.readlines()))))
