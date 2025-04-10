class Publisher:
    def __init__(self, name):
        self.name = name

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display_info(self):
        print(f"Publisher: {self.name}")
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Number of Pages: {self.no_of_pages}")

python_book = Python(name="O'Reilly", title="Learning Python", author="Mark Lutz", price=45.99, no_of_pages=1600)
python_book.display_info()



# Step 1: Start  
# Step 2: Define the Publisher class with 'name' as input.
# Step 3: Define the Book class that inherits Publisher, initializes 'name', 'title', 'author', and calls Publisher.
# Step 4: Define the Python class that inherits Book, initializes 'price' and 'no_of_pages', and calls Book.
# Step 5: Define the display_info method to print book details.
# Step 6: Create an instance of Python class and pass values.
# Step 7: Call display_info to display details.
# Step 8: Stop