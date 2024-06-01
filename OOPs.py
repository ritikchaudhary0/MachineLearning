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

