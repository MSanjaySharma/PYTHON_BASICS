# We use the "class" statement to create a class
class Human:
    # A class attribute (shared by all instances of this class)
    species = "Homo sapiens"

    # Constructor
    # Note that all methods of a class take "self" as the first argument
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name
        # Initialize property
        self._age = 0

    # Instance method
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def greet(self, loud=False):
        if loud:
            print(f"HELLO, {self.name.upper()}")
        else:
            print(f"Hello, {self.name}")

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method "age()" into an read-only attribute of the same name.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age
