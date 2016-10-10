"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   a. Encapsulation.
   This concept means that the data and it's functionality are together in an object.
   It's also can be very helpful if we want some data to have restricted  access
   from the outside representation of the Object.
   It can be accesible only withtin an Object by other componentsself.

   b. Abstraction
   This concept simplifies a big complex data by creating different classes for each
   specific problem solving.
   Also abstraction means data hiding. We know what a class does on a human level of
   understanding, but we don't need to specifically know what is inside the class
   and what information it's method uses inturnally.

   c. Polymorphism
   It is a process of using methods in different ways with different data input.
   For example, we can have different classes that are inheritances from their Parent class.
   They share the same class structure, but they can be interchangeable.
   They can be different.

2. What is a class?

   Object is a single data structure. It contains data and also functions, which called methods.
   Class is a way of organizing and producing objects with similar attributes and methods.

3. What is an instance attribute?

   instance attribute is an attribute that is assigned to a Class instance.
   In this case a Class doesn't have an instance attribute, only it's instance doesn.

4. What is a method?

   Method is a function that is defined within a class.

5. What is an instance in object orientation?

   Instance is an individual object of the class. For example, "Sun" is class Str
   but the string "Sun" is the object/instance of the Str class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attrinbute is the attribute that is assigned to a Class and can be inherited by
   it's instances. But instance attribute is an attribute that can be assigned to an
   instance, but doesn't exist in the Class.

   Class attribute can be very useful in cases when you want to list the attributes all
   instances will inherite and will have in common.

   Instance attributes are good when assigning a specific data to a specific instance.
   That way none of the other instances will share that attribute. Unless you assign it.

"""


# Parts 2 through 5:
# Create your classes and class methods

#Part 2
class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Questions(object):

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Exam(object):

    def __init__(self, name):
        self.question = []
        self.name = name
# Part 3
    def add_question(self, question, answer):
        # didn't understand the part 3 exercise
        pass
