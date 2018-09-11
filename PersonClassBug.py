"""
**********************************************************************
* Filename    : PersonClassBug.py
* Description : Solution to CodeWars PersonClassBug Challenge
* Author      : Pat Alwell
* E-mail      : pat.alwell@gmail.com
* Website     : www.patalwell.com
* Update      :

* Challenge   : The following code was thought to be working properly, however when the code tries to access the age of the person instance it fails.

person = Person.new('Yukihiro', 'Matsumoto', 47)
puts person.full_name
puts person.age

For this exercise you need to fix the code so that it works correctly.
**********************************************************************
"""

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + ' ' + last_name
