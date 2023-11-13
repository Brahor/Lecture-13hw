# Task 1
False == (not True) 

# %%
not (True and "A" == "B")

(True and False) == (True and False)

# Task 2
def total_grain():
    total_grains = 0
    for square in range(64): 
        total_grains += 2**square
    return total_grains

print(total_grain())

total_grains_on_board = total_grain()  
print(total_grains_on_board)

total_grain_weight = ((total_grains_on_board * 0.065)/1000000)  # in tons
print(f"The weight in tons is {total_grain_weight}")


# Task 3
# сам би не зробив, але концуптуально зрозуміло, що відбувається
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# Ask the user for a number
number = int(input("Please enter a number: "))

# Find and print the factors of that number
divisors = factors(number)
print(f"The divisors of {number} are:", divisors)

# Task 4
def determine_triangle_type(a, b, c):
    
    
    # Check for equilateral triangle
    if a == b == c:
        return "Equilateral"
    # Check for isosceles triangle
    elif a == b or a == c or b == c:
        return "Isosceles"
    # If none of the above, then it's scalene
    else:
        return "Scalene"

# Get triangle sides from user input
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))


if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print(f"The triangle is {determine_triangle_type(side1, side2, side3)}.")
else:
    print("The given sides cannot form a triangle.")


# Task 5
def longest_consecutive_symbol(s):
    
    longest_streak_char = s[0]
    longest_streak_length = 1
    
    
    current_streak_char = s[0]
    current_streak_length = 1

    
    for char in s[1:]: 
        if char == current_streak_char:
            
            current_streak_length += 1
        else:
            
            current_streak_char = char
            current_streak_length = 1

        
        if current_streak_length > longest_streak_length:
            longest_streak_char = current_streak_char
            longest_streak_length = current_streak_length

    return longest_streak_char

input_string = 'aaaabiiiiiiiiiiiiiiiiiiichjjjjjswwwxyzaaaaaa'
output = longest_consecutive_symbol(input_string)
print(f'Longest consecutive symbol: {output}')
