# Assignment 3

# Task 1
def triangle_area(x1, y1, x2, y2, x3, y3):
    value = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    area = 0.5 * abs(value)
    return area

# Checking if it works
result = triangle_area(10, 1, 2, 2, 33, 3)
print(result)

# Task 2
import re

test_string = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."

print ("This is original looks like : " + test_string)

res = len(re.findall(r'\w+', test_string))

print ("Amount of words is : " + str(res))

# Task 3
start_string = "snake_case_text" 

import re

words = [word.capitalize() for word in re.split('_','snake_case_text')]

result = ''.join(words)

print(result)  

# Task 4
n = int(input("Enter a number: "))

for fizzbuzz in range(n):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

# Task 5
start_string = "SnakeCaseText" 

import re
result = re.findall('[A-Z][^A-Z]*', 'SnakeCaseText')

end_string = '_'.join(result).lower()

print(end_string)

# Task 6

s1 = input("Enter a word:")
s2 = input("Enter a word again")

def anagrams(s1,s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

anagrams (s1,s2)