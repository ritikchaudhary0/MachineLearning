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

#  Attributes and the Init Method---------------------------------------------------------------------------------------------------------------------------------

class MyList:
    def __init__(self, initial_data):
        self.data = initial_data
        
my_list = MyList([1,2,3,4,5])
print(my_list.data)

Output- [1, 2, 3, 4, 5]

# Creating an Append Method----------------------------------------------------------------------------------------------------------------------------------------

class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        
    # Add method here
    def append(self,new_item):
        self.data = self.data + [new_item]  # if i didn't put list sign to the new_item variale then python will treat it as a int argument. So when i append without list sign it will give me error because list
                                            # and int can't concatanate. means i will get type error. so that's why i put the list sign in the function itself to avoid this error.

my_list = MyList([1, 2, 3, 4, 5])
print(my_list.data)

my_list.append(6)
print(my_list.data)

Output- [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]

# Creating and Updating an Attribute---------------------------------------------------------------------------------------------------------------------------------------------
"""
What we have done so far--

We've created a MyList class that stores a list at the point of instantiation using the init constructor.
We stored that list inside an attribute of MyList called data.
We've created a method — MyList.append() — that mimics the behavior of list.append().
"""

globals().clear()
class MyList:
    pass
class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calculate the initial length
        self.length = 0
        for item in self.data:  #This is there way of callculating the length .
            self.length += 1

    def append(self, new_item):
        self.data = self.data + [new_item]
        # Update the length here
        self.length = len(self.data)   # This is my way of callculating the length using len() function :)
        
my_list = MyList([1,1,2,3,5])
print(my_list.length)

my_list.append(8)
print(my_list.length)

Output:- 5
         6
