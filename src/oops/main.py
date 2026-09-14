"""Main calling script for the OOPS project."""

import classes.animal as an

if __name__ == "__main__":
    ob = an.Animal("Leo", "Lion", 5)
    print(f"Animal Name: {ob.name}")
    print(f"Animal Species: {ob.species}")
    print(f"Animal Age: {ob.age}")
