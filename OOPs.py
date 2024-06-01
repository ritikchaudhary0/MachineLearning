# object-oriented programming (OOP). Rather than designing code around sequential steps, we will design it around objects. 
l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
print(type(l))
print(type(s))
print(type(d))

'''
Output- <class 'list'>
<class 'str'>
<class 'dict'>
'''

# Instantiating a Class--------------------------------------------------------------------------------------------------------------------------------------------------------
globals().clear() # It is a Python method that clears all the global variables from the current global namespace.
class MyClass:
    pass
class MyClass:
    pass

my_instance = MyClass()
print(type(my_instance))


# Creating Methods---------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
In order to make our class do something, we need to define some methods. Methods allow objects to perform actions.
You can think of methods like special functions that belong to a particular class. This is why we call the replace method str.replace()— because the method belongs to the str class.
"""
class MyClass:
    def first_method():
        return "This is my first method"
    
my_instance = MyClass()

#  Understanding "self" -------------------------------------------------------------------------------------------------------------------------------------------------------------

class MyClass:
    
    def first_method(self):
        return "This is my first method"
    
my_instance = MyClass()
result = my_instance.first_method()
print(result)

Output- "This is my first method"

# Creating a Method that Accepts an Argument-------------------------------------------------------------------------------------------------------------------------------------------------

class MyClass:
    
    def first_method(self):
        return "This is my first method"
    
    # Add method here
    def return_list(self, input_list):
        self.input_list = input_list
        return self.input_list
    
my_instance = MyClass()
result = my_instance.return_list([1,2,3])
print(result)

Output- [1, 2, 3]
"""
One more we have to write this above code. But my this down way method work with ony dataquest platform
"""

class MyClass:
    
    def first_method(self):
        return "This is my first method"
    
    # Add method here
    def return_list(self, input_list):
        return input_list
    
my_instance = MyClass()
result = my_instance.return_list([1,2,3])
print(result)

Output - [1, 2, 3]

