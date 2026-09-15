"""Animal class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass
