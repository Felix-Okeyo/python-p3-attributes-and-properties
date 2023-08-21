#!/usr/bin/env python3

# List of approved dog breeds
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

# Dog class
class Dog:
    def __init__(self):
        self._name = None
        self._breed = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")


# # test cases
# dog1 = Dog()
# dog1.name = "French Bulldog"
# print("Dog 1's name:", dog1.name)

dog2 = Dog()
dog2.breed = "marti"
print(dog2.breed)