#!/usr/bin/env python3

class Person:
    # Class body goes here

    #Instance method definition
    def talk(self):
        return "Hello World!"
    def walk(self):
        return "The person is walking."

person = Person()
print(person.walk())
print(person.talk())