# question 1:

# create a class representing book.
# add attributes and methods to the class.
# use contructors to initialize each object with unique values
# add inheritance layer to explore polymorphism or encapsulation.

class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.current_page = 0

    def read(self, pages):
        if pages < 0:
            print("Cannot read negative pages.")
            return
        self.current_page += pages
        print(f"Reading '{self.title}': You have read {pages} pages. Current page: {self.current_page}")

        if self.current_page > 100:
            print(f"You have finished reading '{self.title}' by {self.author}!")

# creating objects with unique attribues
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
book2 = Book("1984", "George Orwell", 1949, "Dystopian")

print(f"book1:{book1.title}, {book1.author}, {book1.publication_year}, {book1.genre}")
print(f"book2:{book2.title}, {book2.author}, {book2.publication_year}, {book2.genre}")
 
# using methods to read pages
book1.read(50)
book2.read(100)
book1.read(-10)  
book2.read(20)

#question 2:
#Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving", while Plane.move() prints "Flying").

class Car:
    def move(self):
        return("Driving")
class Horse:
    def move(self):
        return("Galloping")
class Plane:
    def move(self):
        return("Flying")
class Boat:
    def move(self):
        return("Sailing")
class Bicycle:
    def move(self):
        return("Pedaling")
#polymorphism in action
for vehicle in (Car(), Horse(), Plane(), Boat(), Bicycle()):
    print(vehicle.move())