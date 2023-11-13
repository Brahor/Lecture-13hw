# Task 1
print(10 > 5)
print(42 != "42")
print(3 <= 4)

# Coding. Task 1
# Print the text in which there will be a quote with double quotes.
print('Hey hey, here are the "" in my text')

# Coding. Task 2
def Palindrome(a):
 return a == a[::-1]

a = input("Enter anything you want: ")
other = Palindrome(a)

if other:
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")

# Coding. Task 3.
# by listing all the parameters in the print functions
name = input("What is your name?:")
age = input("What is your age?:")

print("Your name is", name, "and you are", age, "years old")

# by formatting a string using the format function
name = input("What is your name again?:")
age = input("What is your age again?:")

name_age_template = "Your name is {} and you are {} years old"
formatted_name_age = name_age_template.format(name, age)
print(formatted_name_age)

# by formatting a string with f-string
name = input("What is your name again2?:")
age = input("What is your age again2?:")

name_age = (f"Your name is {name} and you are {age} years old")
print(name_age)

# Coding. Task 4.
string_1 = "Animals  "
lowercased_string_1 = string_1.lower()
print(lowercased_string_1)

string_2 = "  Badger"
capital_string_2 = string_2.upper()
print(capital_string_2)

# A
string_3 = "   HoneyPot   "
no_space_string_3 = string_3.lstrip()
print(no_space_string_3)

# B
string_3 = "   HoneyPot   "
no_space_string_3 = string_3.rstrip()
print(no_space_string_3)


# C
string_3 = "   HoneyPot   "
no_space_string_3 = string_3.strip()
print(no_space_string_3)

# Does the string start with "Be"

strings = ["Bear", "bear", "BEAR", "bEar"]

for loop in strings:
    if loop.startswith('Be'):
        print(f"'{loop}' starts with 'Be'")
    else:
        print(f"'{loop}' does not start with 'Be'")

# All other strings start with Be
string_2 = "bear"
formatted_string2 = string_2.capitalize()
print(formatted_string2)

string_3 = "BEAR"
formatted_string3 = string_3.capitalize()
print(formatted_string3)

string_4 = "bEar"
formatted_string4 = string_4.capitalize()
print(formatted_string4)

