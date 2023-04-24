# Create an empty dictionary to store book orders
book_orders = {}

# Define a function to add a new book order to the dictionary
def add_order(book_title, quantity):
    if book_title in book_orders:
        # If the book is already in the dictionary, add the quantity to the existing value
        book_orders[book_title] += quantity
    else:
        # If the book is not in the dictionary, create a new key-value pair with the quantity
        book_orders[book_title] = quantity

# Define a function to remove a book order from the dictionary
def remove_order(book_title, quantity):
    if book_title in book_orders:
        if book_orders[book_title] > quantity:
            # If the quantity to remove is less than the existing quantity, subtract the quantity from the value
            book_orders[book_title] -= quantity
        else:
            # If the quantity to remove is greater than or equal to the existing quantity, remove the key-value pair
            del book_orders[book_title]

# Define a function to print the current book orders
def print_orders():
    print("Current book orders:")
    for book_title, quantity in book_orders.items():
        print(f"{book_title}: {quantity}")

# Test the functions with sample data
add_order("The Great Gatsby", 5)
add_order("To Kill a Mockingbird", 3)
add_order("Pride and Prejudice", 2)
print_orders()  # should print "Current book orders:\nThe Great Gatsby: 5\nTo Kill a Mockingbird: 3\nPride and Prejudice: 2\n"
remove_order("To Kill a Mockingbird", 2)
print_orders()  # should print "Current book orders:\nThe Great Gatsby: 5\nPride and Prejudice: 2\n"
add_order("The Great Gatsby", 3)
print_orders()  # should print "Current book orders:\nThe Great Gatsby: 8\nPride and Prejudice: 2\n"
