class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")


# Example usage
my_dog = Dog("Buddy", 3)
my_dog.bark()
print(f"{my_dog.name} is {my_dog.age} years old.")
