# assignemnt 8


#task 1
def apply_operation(operation, operand1, operand2):
    return operation(operand1, operand2)

def operation(x, y):
    return x + y

# Testing the function
result = apply_operation(operation, 2, 3)
print(result)  
def operation(x, y):
    return x * y

# Testing the function
result = apply_operation(operation, 2, 3)
print(result)  


#task 2

def get_multiplier(multiplier):
    def inner_get_multiplier(number):
        return number * multiplier
    return inner_get_multiplier

# testing
double = get_multiplier(2)  
triple = get_multiplier(3)  

# results
print(double(5)) 
print(triple(5)) 



# task 3
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

operation_list = [add,subtract,multiply]

num1 = 10
num2 = 5

for operation in operation_list:
    result = operation(num1, num2)
    print(f"Result of {operation.__name__}({num1}, {num2}): {result}")


# task 4

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


operation_dict = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply
}


operation = input("Enter operation (add, subtract, multiply): ")
while operation not in operation_dict:
    print("Invalid operation. Try again.")
    operation = input("Enter operation (add, subtract, multiply): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


result = operation_dict[operation](num1, num2)
print(f"Result of {operation}({num1}, {num2}): {result}")


