class Student:
    # this 'self' variable needs to be added to each method. It's essentially 'this' and doesn't have to be named self. But that in convention
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # basically the toString method
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."
    
    # Tells devs we're printing an object. Something for the debugger. If there is no __str__ function, this will be used
    # unambiguous representation to recreate the object
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

student = Student("Rolf", 12)