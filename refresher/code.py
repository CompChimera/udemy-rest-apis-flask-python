#  Random tests and notes during the review portion
price = 9.9
x = 3

result = price * x

print("Example printing variable with value")
print(result)

print("-------")


name = "Torgal"
# sets value at time of evaluation
greeting = f"{name} is best boy" 
greetingTemplate = "Hello {}"
print("Practising string formatting: ")
print(greetingTemplate.format(name))

print("-------")

# Getting input
print("Practising getting user input: ")
size_input = input("How big is your house (in square feet): ")
# you'll get back a string everytime - we'll need to conver the input into a number
square_feet = int(size_input)
square_meters = square_feet / 10.8

resultString = "{} square feet is equal to {} square meters"
print(resultString.format(square_feet, square_meters))
# var:.2f will round to 2 decimal points as best it can
print(f"{square_feet} square feet is equal to {square_meters:.2f} square meters")

print("-------")

# set functions
friends = {"bob"}
abroad = {"anne"}
#  this will take the set {friends} and remove {abroad}
local_friends = friends.difference(abroad)

# both = friends.intersection(abroad) gives you the elements that are the same between the sets


# functions - keyword arguments
def divide(dividend, divisor):
    return (dividend/divisor)

# Keyboard arguments are calling the function as below with the name of the parameters from the function definition. 
#  This allows you to put them in any order (with positional arugments first, if any) and gives context to readers. 
#  Common standard in Python
divide(dividend=5, divisor=5)


#  Unpacking variable
# say we have a function as so 
def add(x, y):
    return x + y

nums = {"x": 15, "y": 20}
# Lecture 31 
# ** will _collect_ things when used as a func parameter.
#** used in an _argument_  will unpack the dictionary to put the data in the argument as x: 15, y: 20 
# and because they are the same names as the named parameters in the function definition, it will add them as named arguments
#  This need have to have the same name of items as parameters that the function takes in or else it will cause an error
add(**nums)

# Need to be careful if a function is unpacking args, you likely may need to do it again when calling another function within that function
#  Otherwise it will send a tuple, and the second function will create a tuple of tuple which.. Is not what we want. 
#  The example was a multiply function, and when multiplying 1 * a tuple, it returns the tuple

#  String formatting
#  This !r will automatically wrap the variable output in quotationmarks for you
#  <Student 'rolfe'>
testName = "rolfe"
testString = f"<Student {testName!r}>"
print(testString)


# Making functions secure
#  @ syntax:
#  Adding `@make_secure` ensures a function requires a decorator to be run
# There are some intricinces with this - need to use @functools.wraps(func) in the make_secure function to ensure things under the hood stay the same for the function name
# -- keeping function name and docstring  --
import functools


user = {"username": "brittany", "access_level": "user"}


def make_secure(func):
    # Doesn't handle parameters - needs a slightly different solution shown in comments
    @functools.wraps(func)
    def secure_function():
        # def secure_function(*args, **kwargs)
        if user["access_level"] == "admin":
            # return func(*args, **kwargs)
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
# parameter example
#  def get_admin_secret(access_level):
def get_admin_secret():
    return "SECRET: Have a good day <3"

print("Checking admin status for '{}'".format(user['username']))
print(get_admin_secret())
user = {"username": "brittany", "access_level": "admin"}

print("Checking admin status for '{}'".format(user['username']))
print(get_admin_secret())

#  To get a full working decorator with different inputs, we need to add another layer to make_secure
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."

        return secure_function

    return decorator


@make_secure("admin")  # This runs the make_secure function, which returns decorator. Essentially the same to doing `@decorator`, which is what we had before.
def get_admin_secret2():
    return "admin: Add some more motivating welcomes for your users next week"


@make_secure("user")
def get_dashboard_secret2():
    return "user: Have a great week!"

print("Checking access level for '{}'".format(user['username']))

print(get_admin_secret2())
print(get_dashboard_secret2())

user = {"username": "anna", "access_level": "user"}

print("Checking access level for '{}'".format(user['username']))

print(get_admin_secret2())
print(get_dashboard_secret2())


# Classes and init parameters
#  if you have something like
# def __init__(self, name: str, grades: List[int] = [])
#  This does NOT set a default value to empty list per instance of class
#  It links all instances to use the same list for grades. So if one student has a grade and the other one doesn't but you print both students...
# ...both students now have the same grade
#  Set any default values within the __init__ function itself and not in the method definition