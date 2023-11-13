#Assignment 11

# Task 1

# Create a function named "add_to_shopping_list" that maintains a shopping list. 
# It should take a list and a tuple containing an item and its quantity and return the updated list
def add_to_shopping_list(shopping_list, item_tuple):
   
    
    for index, (item, quantity) in enumerate(shopping_list):
        if item == item_tuple[0]:
            
            shopping_list[index] = (item, quantity + item_tuple[1])
            break
    else:
        
        shopping_list.append(item_tuple)
    
    return shopping_list

# Testing
my_list = [("apples", 2), ("bananas", 5)]
print(add_to_shopping_list(my_list, ("oranges", 3)))  # [('apples', 2), ('bananas', 5), ('oranges', 3)]
print(add_to_shopping_list(my_list, ("bananas", 2)))  # [('apples', 2), ('bananas', 7), ('oranges', 3)]

#Task 2

# Implement a function "email_validator" that validates a list of emails and returns a list of valid emails. 
# Valid emails should only include those with the domain "gmail.com."

import re

emails_list = ['qwerty@gmail.com', 'abyrvalg.@.com', 'zgyyn@gmail.com', 'contraspemspero@ukr.ua', 'dfwefwfe2']

def email_validator(emails):
    
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
    
    
    valid_emails = [email for email in emails if pattern.match(email)]
    
    return valid_emails

gmail_emails = email_validator(emails_list)
print(gmail_emails)


# Task 3
# Write a function named "find_missing_number" that takes a list of consecutive (increasing) numbers and finds the missing number from the range 1 to n (inclusive). 
# Use assertions to validate input and output".

def find_missing_number(L):
    # Assertions for input
    assert L, "The list should not be empty"
    assert all(isinstance(i, int) for i in L), "All elements in the list should be integers"
    assert L[0] == 1, "The list should start with 1"
    
    start, end = L[0], L[-1]
    missing_elements = sorted(set(range(start, end + 1)).difference(L))
    
    # Assertion for output
    expected_missing = [6, 7, 9]
    assert missing_elements == expected_missing, f"Expected {expected_missing} but got {missing_elements}"

    return missing_elements


numbers_list = [1, 2, 3, 4, 5, 8, 10]
print(find_missing_number(numbers_list))


# Task 4


def grade_students(students, threshold):
   
    above_threshold = [name for name, grade in students if grade > threshold]
    return above_threshold

# Testing the function:
students_grades = [("Danylo", 85), ("Misha", 90), ("Kyrylo", 78), ("Sara", 92)]
threshold_value = 80
print(grade_students(students_grades, threshold_value))  

# Task 5
# Implement a function "book_tracker" that takes a list of book transactions. 
# Each transaction should be a tuple consisting of the book title and a boolean indicating whether it was borrowed (True) or returned (False).

def book_tracker(transactions):
    borrowed_books = []  

    for book_title, is_borrowed in transactions:
        if is_borrowed:
            borrowed_books.append(book_title) 
        else:
            if book_title in borrowed_books:
                borrowed_books.remove(book_title)

    return borrowed_books 



transactions = [("Dutch Republic: Its Rise, Greatness and Fall", True), ("Maxims and thoughts of the prisoner of Saint Helenas", True), ("Praise of Folly", False)]


borrowed_books = book_tracker(transactions)


print(borrowed_books)

# Task 6
def manage_contacts(contacts, action, name, phone_number=None):
    if action == "add":
        
        if not any(contact[0] == name for contact in contacts):
            contacts.append((name, phone_number))
    elif action == "remove":
        
        contacts[:] = [contact for contact in contacts if contact[0] != name]
    elif action == "update":
        
        for i, contact in enumerate(contacts):
            if contact[0] == name:
                contacts[i] = (name, phone_number)
    else:
        print("Invalid action. Please use 'add', 'remove', or 'update'.")

# Testing:
my_contacts = [("Alice", "123-456-7890"), ("Bob", "987-654-3210")]


manage_contacts(my_contacts, "add", "Charlie", "555-555-5555")


print(my_contacts)


# Task 7

def flight_itinerary(flight_routes):
    
    itinerary = []

    
    for route in flight_routes:
        source, destination = route
        itinerary.append(source)
        itinerary.append(destination)

    
    return " -> ".join(itinerary)

# Test
my_flight_routes = [("New York", "Kyiv"), ("Kyiv", "Los Angeles"), ("Los Angeles", "Dnipro")]
itinerary = flight_itinerary(my_flight_routes)
print(itinerary)  