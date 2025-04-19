# question 1

class Book:
    def __init__(self, title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_pages(self):
        print ("Over 200pages.")

class novel(Book):
    def display_pages(self):
        print("The novel has 500 pages.")
class atlas(Book):
    pass
class autobiography(Book):
    def display_pages(self):
        print("The book has 600 pages.")
class comic_book(Book):
    def display_pages(self):
        print("The comic book has 100pages.")

Novel = novel("War and Peace", "Tolstoy", 1869)
Atlas = atlas("The North Carolina Atlas", "Douglas Orr", 2000)
Autobiography = autobiography("I Am Malala", "Malala Yousafzai", 2013)
Comic_book= comic_book("Blueberry", "Jean Michel", 2015)

for x in (Novel, Atlas, Autobiography, Comic_book):
    print(f"{x.title} written by {x.author} in the year {x.publication_year}.")
    x.display_pages()

#question 2   

class Dog:

    def make_sound(self):
        print("Woof! Woof!")

class Cat:

    def make_sound(self):
        print("Meow! Meow!")
class Lion:

    def make_sound(self):
        print("Roar! Roar!")

for x in (Dog(), Cat(), Lion()):
    x.make_sound()