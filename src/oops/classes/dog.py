from classes.animal import Animal


class Dog(Animal):
    """Dog class inheriting from Animal class."""

    def __init__(self, name, species, age, breed):
        super().__init__(name, species, age)
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    # This method is added to provide a string representation of the Dog object
    def __str__(self):
        return f"Dog(Name: {self.name}, Species: {self.species}, Age: {self.age}, Breed: {self.breed})"
