# main.py
from models import Book, Member, Magazine, DVD  # TODO: also import Magazine, DVD
book = Book("Python 101", 1, "A. Rao")
# TODO: create one Magazine and one DVD
magazine = Magazine("Python weekly",2,154)
dvd = DVD("Python tutorials",3,60)
book2 = Book("Python Interview Prep",4,"Tata")
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. TODO: trigger the borrow-limit error and the not-borrowed error, catching each
try:
    alice.borrow(magazine)
    alice.borrow(dvd)
    alice.borrow(book2)
except ValueError as e:
    print("Borrow-limit reached:",e)

print("Borrowed by Alice:",alice.borrowed_titles())
print("Borrowed by Bob:",bob.borrowed_titles())

try: 
    print(f"Alice returns {book.title} with late-fee => {alice.return_item(book)}")
    print(f"Bob returns {book.title} with late-fee => {bob.return_item(book)}")
except ValueError as e:
    print("Not-Borrowed:",e)

# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]  # TODO: add the magazine and the DVD
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)

#Access __available and fall back to  is_available()
try:
    print("Book available?",book.__available)
except AttributeError as e:
    print("Attribute error:",e)
    print("Book available?",book.is_available())