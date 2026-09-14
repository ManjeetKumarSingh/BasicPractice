"""Main calling script for the OOPS project."""

from classes.dog import Dog
from classes.animal import Animal

if __name__ == "__main__":
    ob = Animal("Leo", "Lion", 5)
    print(f"Animal Name: {ob.name}")
    print(f"Animal Species: {ob.species}")
    print(f"Animal Age: {ob.age}")
    print("*" * 40)
    dog = Dog("Zoeee", "Dog", 3, "Golden Retriever")
    print(f"Complete Dog Details: {dog}")
