"""Dictionary Operations in Python"""

from typing import TypedDict

# Creating a dictionary
dict1 = {"name": "John", "age": 30, "city": "New York"}
print(dict1)


class User(TypedDict):
    name: str
    age: int
    city: str


def add_key_value(dictionary, key, value) -> None:
    """Add a key-value pair to the dictionary."""
    dictionary[key] = value
    return dictionary


def update_key_value(dictionary, key, value) -> User:
    """Update the value of an existing key in the dictionary."""
    if key in dictionary:
        dictionary[key] = value
    else:
        print(f"Key '{key}' not found in the dictionary.")
    return dictionary
