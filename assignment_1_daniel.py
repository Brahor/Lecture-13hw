# assignment 3

a = 4
b = 5

print(a)
print(b)

# Swapping number one
a = a + b
b = a - b
a = a - b

print(a)
print(b)

# Swapping number two
a, b = b, a

# Swapping number three
a = 7
b = 5

a = a * b  # a becomes 15
b = a / b  # b becomes 3
a = a / b  # a becomes 5

print(a)
print(b)

# assignment 2


def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Enter a real number,pls!")


number_one = get_number('Enter number one: ')
print(number_one)

number_two = get_number('Now number two: ')
print(number_two)

delta = number_one - number_two
print(delta)


# assignment 3
def get_number(promt):
    while True:
        try:
            value = float(input(promt))
            return value
        except ValueError:
            print("Enter an actual number!")



number_1 = get_number('Enter stuff:')
print(number_1)

number_2 = get_number('Enter a number again:')
print(number_2)

largest_number = max(number_1, number_2)
print(largest_number)
