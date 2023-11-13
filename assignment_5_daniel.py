# Task 1
def prime_dich(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes(a, b):
    primes = []
    for num in range(a, b+1):  # b+1 because I want to include b
        if prime_dich(num):
            primes.append(num)
    return primes

print(find_primes(10,30))

# Task 2
def unique_characters(s):
    for char in s:                 
        if s.count(char) > 1:     
            return False         
    return True                   

print(unique_characters("ABYRVLG"))

# Task 3
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    fib_prev, fib_curr = 0, 1  
    
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next
    
    return fib_curr

# Testing
print(fibonacci(10))  


# Task 4
def swapcase(input_string: str) -> str:
    result = ''  
    
    for char in input_string:
        
        if char.isupper():
            result += char.lower()
        
        elif char.islower():
            result += char.upper()
        
        else:
            result += char

    return result

# Testing
print(swapcase('LmOJSDNOJSDN!'))  

# Task 5
def simple_interest(initial_amount, interest_rate, years):
    amount = initial_amount
    for _ in range(years): 
        interest_for_year = amount * interest_rate
        amount += interest_for_year  
    return round(amount, 2) 

# Testing
print(simple_interest(10000, 0.1, 15))
