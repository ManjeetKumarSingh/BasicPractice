"""Main calling script for the OOPS project."""

from classes.baseclasses.dog import Dog

if __name__ == "__main__":
    print("*" * 40)
    dog = Dog("Zoeee", "Dog", 3, "Golden Retriever")
    print(f"Complete Dog Details: {dog}")
