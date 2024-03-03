#  Random tests and notes during the review portion
price = 9.9
x = 3

result = price * x

print(result)


name = "Torgal"
# sets value at time of evaluation
greeting = f"{name} is best boy" 
greetingTemplate = "Hello {}"
print(greetingTemplate.format(name))

# Getting input
size_input = input("How big is your house (in square feet): ")
# you'll get back a string everytime - we'll need to conver the input into a number
square_feet = int(size_input)
square_meters = square_feet / 10.8

resultString = "{} square feet is equal to {} square meters"
print(resultString.format(square_feet, square_meters))
# var:.2f will round to 2 decimal points as best it can
print(f"{square_feet} square feet is equal to {square_meters:.2f} square meters")


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