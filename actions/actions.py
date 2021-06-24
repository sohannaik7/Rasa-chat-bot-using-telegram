# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"
import webbrowser
from typing import Any, Text, Dict, List

import wikipedia
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

global domain
domain = ' python'


class Actionoops(Action):
    def name(self) -> Text:
        return "action_about_oops"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'oops':
                name = e['value']
                message = ""
                name = name.lower()
            if name == 'class' or name == 'clas' or name == 'classes':
                message = "A class is a blueprint that defines the variables and the methods" \
                          " (Characteristics) common to all objects of a certain kind." \
                          "Example: If Car is a class, then Audi A6 is an object of the Car class." \
                          " All cars share similar features like 4 wheels, 1 steering wheel, windows, breaks etc." \
                          " Audi A6 (The Car object) has all these features."
            elif name == 'object' or name == 'objects':
                message = "The object is an entity that has a state and behavior associated with it." \
                          " It may be any real-world object like the mouse, keyboard, chair, table, pen, etc." \
                          " Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects." \
                          " More specifically, any single integer or any single string is an object."
            elif name == 'inheritance' or name == 'inherit':
                message = "Inheritance is a way of creating a new class for using details of an existing class without modifying it." \
                          " The newly formed class is a derived class (or child class). Similarly," \
                          " the existing class is a base class (or parent class)."
            elif name == 'encapsulation' or name == 'encapsul':
                message = "Using OOP in Python, we can restrict access to methods and variables." \
                          " This prevents data from direct modification which is called encapsulation." \
                          " In Python, we denote private attributes using underscore as the prefix i.e single" \
                          " _ or double __."
            elif name == 'polymorphism' or name == 'polymorph':
                message = "Polymorphism contains two words 'poly' and 'morphs'." \
                          "Poly means many, and morph means shape. By polymorphism, we understand that one task can " \
                          "be performed" \
                          "in different ways. For example - you have a class animal, and all animals speak. But they " \
                          "speak differently. "
            elif name == 'abstraction' or name == 'abstract' or name == 'data abstraction':
                message = "Abstraction is used to hide internal details and show only functionalities." \
                          " Abstracting something means to give names to things so that the name captures" \
                          " the core of what a function or a whole program does." \
                          "Data abstraction and encapsulation both are often used as synonyms." \
                          " Both are nearly synonyms because data abstraction is achieved through encapsulation."
            elif name == 'Constructor' or name == 'constructorr':
                message = "A constructor is a special type of method (function)" \
                          " which is used to initialize the instance members of the class" \
                          "Constructor definition is executed when we create the object of this class." \
                          "Constructors also verify that there are enough resources for the object to perform any " \
                          "start-up task. "
            elif name == 'types of constructor':
                message = "1. Parameterized Constructor " \
                          "2. Non-parameterized Constructor"
            elif name == 'Parameterized' or name == 'non-Parameterized' or name == 'non Parameterized':
                message = "The non-parameterized constructor uses when we do not want to manipulate the value" \
                          " or the constructor that has only self as an argument." \
                          "The parameterized constructor has multiple parameters along with the self."

        dispatcher.utter_message(text=message)
        return []


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#         return []
class actionfunction(Action):
    def name(self) -> Text:
        return "action_function"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'function':
                name = e['value']
                message = ""
            if name == 'function' or name == 'functions':
                message = "A function in Python is an aggregation of related statements designed to perform a " \
                          "computational," \
                          " logical, or evaluative task. The idea is to put some commonly or repeatedly" \
                          " done task together and make a function so that instead of writing the same code" \
                          " again and again for different inputs, we can call the function to reuse code contained" \
                          " in it over and over again......def function_name(parameters):"
            elif name == 'class method' or name == 'class':
                message = "The @classmethod decorator, is a builtin function decorator that is an expression" \
                          " that gets evaluated after your function is defined. The result of that evaluation " \
                          "shadows your function definition ':class C(object):@classmethoddef fun(cls, arg1, arg2, " \
                          "...):" \
                          "....fun: function that needs to be converted into a class methodreturns:" \
                          " a class method for function."
            elif name == 'static method' or name == 'static':
                message = "A static method is also a method which is bound to the class and not the object" \
                          " of the class.A static method can’t access or modify class state." \
                          "It is present in a class because it makes sense for the method to be " \
                          "present in " \
                          "class.class C(object):" \
                          "@staticmethoddef fun(arg1, arg2, ...):" \
                          "...returns: a static method for function fun"
        dispatcher.utter_message(text=message)
        return []


class actionfunction(Action):
    def name(self) -> Text:
        return "action_exception"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'exception':
                name = e['value']
                message = ""
            if name == 'exceptions' or name == 'exception':
                message = "In Python, exceptions can be handled using a try statement. " \
                          "The critical operation which can raise an exception is placed inside the try clause. " \
                          "The code that handles the exceptions is written in the except clause. " \
                          "We can thus choose what operations to perform once we have caught the exception            " \
                          "  ." \
                          "An exception can be defined as an unusual condition in a program resulting in the " \
                          "interruption " \
                          "in the flow of the program. If we do not handle the exception, the interpreter doesn't " \
                          "execute " \
                          "all the code that exists after the exception"
            elif name == 'try' or name == 'trys':
                message = "The try block lets you test a block of code for errors. " \
                          "The except block lets you handle the error. The finally block lets you " \
                          "execute code, regardless of the result of the try- and except blocks."
            elif name == 'catch' or name == 'except':
                message = "except is used to catch and handle the exception(s) that are encountered in " \
                          "the try clause. else lets you code sections that should run " \
                          "only when no exceptions are encountered in the try clause."
        dispatcher.utter_message(text=message)
        return []


class actionfunction(Action):
    def name(self) -> Text:
        return "alldatatypes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'datatypepython':
                name = e['value']
                message = ""
            if name == 'integer' or name == 'integers':
                message = "In Python, integers are zero, positive or negative whole numbers without a fractional" \
                          " part and having unlimited precision, e.g. 0, 100, -10. The followings are valid integer" \
                          " literals in Python jsut----hello = 5"
            elif name == 'string' or name == 'strings':
                message = "String. In Python, string is an immutable sequence data type. It is the sequence of " \
                          "Unicode characters wrapped inside single," \
                          " double, or triple quotes." \
                          " The followings are valid string literals in Python ----hello = '' "
            elif name == ' floating' or name == 'float':
                message = "The Python float() method converts a number stored in a string or integer into a floating " \
                          "point number," \
                          "or a number with a decimal point. Python floats are useful for any function that requires " \
                          "precision," \
                          " like scientific notation. Programming languages use various data types to store values"
            elif name == ' input' or name == 'output' or name == 'print':
                message = "Sometimes a developer might want to take input from the user at some point in the program." \
                          " To do this Python provides an input() function. Syntax: input('prompt') where," \
                          " prompt is a string that is displayed on the string at the time of taking input. " \
                          " Example 1: Taking input from the user with a message----m = input('enter the number')" \
                          "example 2: printing the output print('hello world')"
            elif name == 'datatype' or name == 'datatypes':
                message = "Data types are the classification or categorization of data items." \
                          " It represents the kind of value that tells what operations can" \
                          " be performed on a particular data. Since everything is an object in Python programming," \
                          " data types are actually classes and variables are instance (object) of these classes"
            elif name == 'variable' or name == 'variables':
                message = "Variables are nothing but reserved memory locations to store values." \
                          " This means that when you create a variable you reserve some space in memory." \
                          " Based on the data type of a variable, the interpreter allocates memory and decides " \
                          "what can be stored in the reserved memory." \
                          "variable are independent in python"
            elif name == 'operator' or name == 'operators':
                message = "An operator, in computer programing, is a symbol that usually " \
                          "represents an action or process. These symbols were adapted from mathematics and logic." \
                          " An operator is capable of manipulating a certain value or operand" \
                          "We have 7 assignment operators- one plain, and seven for the 7 arithmetic python operators" \
                          "1. Arithmetic operators   2. Assignment operators, 3. Comparison operators 4. Logical " \
                          "operators 5. Identity operators 6. Bitwise operators 7. Membership operators "
            elif name == 'branching' or name == 'if' or name == 'else':
                message = "Python if Statement is used for decision-making operations. " \
                          "It contains a body of code which runs only when the condition given in the if statement is " \
                          "true." \
                          " If the condition is false, then the optional else statement " \
                          "runs which contains some code for the else condition." \
                          "if condition: then statement else: then other statement"
            elif name == 'loop' or name == 'loops' or name == 'for' or name == 'while':
                message = "a loop is a programming structure that repeats a sequence of instructions until a specific " \
                          "condition is met." \
                          " Programmers use loops to cycle through values, add sums of numbers, repeat functions," \
                          "and many other things. ... Two of the most common types of loops are the while loop and " \
                          "the for loop" \
                          "for i in range (0,10): print i" \
                          "while condition:" \
                          "statement"

        dispatcher.utter_message(text=message)
        return []
