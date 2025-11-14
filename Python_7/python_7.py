class Hospital:
    def __init__ (self, location, year, capacity):
        self.location = location
        self.year = year
        self.capacity = capacity

Hospital1 = Hospital("Gothenburg", 1899, 650)
Hospital2 = Hospital("Stockholm", 1964, 2200)

print(f"The hospital is located in {Hospital1.location}")

class VideoGame:
    def __init__ (self, developers, year, mode):
        self.developers = developers
        self.year = year
        self.mode = mode

VideoGame1 = VideoGame("EA sport", 1985, "Offline")
VideoGame2 = VideoGame("SEGA", 1964, "Offline")

print(f"The video game was developed by {VideoGame1.developers}")

class University:
    def __init__ (self, location, year, alumni):
        self.location = location
        self.year = year
        self.alumni = alumni

University1 = University("EA sport", 1985, "Offline")
University2 = University("SEGA", 1964, "Offline")

print(f"The university has {University1.alumni}" alumni)

class Book
    def __init__ (self, title, author, year)
        self.title = title
        self.author = author
        self.year = year

Book1 = Book("", "", "")

print(f"The book's title is {Book1.title}")