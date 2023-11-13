
# Task 1
def give_number():
    number = input("Please write a number:")
    return number

def integer_convert(number):
    while True:  
        try:
            converted_integer = int(number)
            return converted_integer  
        except ValueError:  
            print("That's not a valid integer! Please try again.")
            number = input("Please write a number: ")  

# testing if code works

user_input = give_number()
integer_value = integer_convert(user_input)
print(integer_value)

# Task 2
def string_integer():
    string = input("Please write some word:")

    while True:
        try:
            number = int(input("Please enter a number:"))
            
            _ = string[number]
            return string, number
        except ValueError:
            print("Make sure it's a number.")
        except IndexError:
            print(f"The number must be between 0 and {len(string) - 1}.")

def character_print(text, num):
    try:
        character = text[num]
        print(character)
    except IndexError:  
        
        
        print(f"The number must be between 0 and {len(text) - 1}.")

text, num = string_integer()
character_print(text, num)


# Task 3
balance = 1000

def transaction(amount,_type):
    def deposit(amount):
        new_balance_1 = (balance+amount)
        print(new_balance_1)

    def withdrawal(amount):
        new_balance_2 = (balance - amount)
        print(new_balance_2)

    if _type == 'deposit':
        deposit(amount)
    elif _type == 'withdrawal':
        withdrawal(amount)
    else:
        print("Invalid transaction type")

# checking
transaction(500, 'withdrawal')
transaction(250, 'deposit')

# Task 4
import random

dice_result = random.randint(1, 6)
print("It isss:", dice_result)

# Task 5
import random

roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(1000):
    roll_result = random.randint(1, 6)
    roll_counts[roll_result] += 1


for number, count in roll_counts.items():
    print(f"Number {number}  rolled {count} amount of times.")



# Task 6
import random

def get_region_results(rating):
    votes_for_first = sum(1 for _ in range(10000) if random.random() < rating/100)
    return votes_for_first, 10000 - votes_for_first

def main():
    num_regions = int(input("Enter the number of regions: "))

    total_votes_first = 0
    total_votes_second = 0

    for i in range(num_regions):
        rating = float(input(f"Enter a rating for the 1st candidate in region {i+1} (0-100): "))
        votes_first, votes_second = get_region_results(rating)

        print(f"Region {i+1}: {votes_first} votes for the 1st candidate, {votes_second} votes for the 2nd candidate")
        
        total_votes_first += votes_first
        total_votes_second += votes_second

    total_votes = total_votes_first + total_votes_second
    if total_votes_first > total_votes_second:
        print(f"Result: 1st candidate won with {total_votes_first} votes and {100 * total_votes_first / total_votes:.2f}% of all votes")
    else:
        print(f"Result: 2nd candidate won with {total_votes_second} votes and {100 * total_votes_second / total_votes:.2f}% of all votes")

main()
