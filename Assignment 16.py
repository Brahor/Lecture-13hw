# Assignment 1
from functools import wraps

def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('user_type') != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper

@is_admin
def show_customer_receipt(*args, **kwargs):
    print("Receipt shown: some very dangerous operation")

# Testing the decorator
try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e)

try:
    show_customer_receipt(user_type='admin')
except ValueError as e:
    print(e)


# Assignment 2

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {e.__class__.__name__} {str(e)}")
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})

some_function_with_risky_operation({'key': 'bar'})
