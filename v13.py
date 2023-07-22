# Classes
from human import Human
from superhero import Superhero
from batman import Batman

#! Base class
# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == "__main__":
    # Instantiate the class
    i = Human(name="Ian")
    i.say("hi")  # Call an instance method; prints "Ian: hi"
    i.greet()  # Call an instance method; prints "Hello, Ian"

    # Instantiate the class again
    j = Human("Joel")
    j.say("hello")  # Call an instance method; prints "Joel: hello"
    j.greet(loud=True)  # Call an instance method; prints "HELLO, JOEL!"
    # i and j are instances of type Human, or in other words: they are "Human" objects

    # Call our class method
    i.say(i.get_species())  # Prints "Ian: H. sapiens"

    # Change the shared attribute
    Human.species = "Homo neanderthalensis"
    i.say(i.get_species())  # Prints "Ian: H. neanderthalensis"
    j.say(j.get_species())  # Prints "Joel: H. neanderthalensis"

    # Call the static method
    print(Human.grunt())  # Prints "*grunt*"

    # Cannot call static method with instance of object
    # because i.grunt() will automatically put "self" (the object i) as an argument
    print(
        i.grunt()
    )  # Prints "TypeError: grunt() takes 0 positional arguments but 1 was given"

    # Update the property for this instance
    i.age = 42
    # Get the property
    i.say(i.age)  # Prints "Ian: 42"
    j.say(j.age)  # Prints "Joel: 0"
    # Delete the property
    del i.age

    # i.age                         # This would raise an AttributeError


#! Inheritance
# Inheritance allows new child classes to be defined that inherit methods and variables from their parent class.
if __name__ == "__main__":
    sup = Superhero(name="Flash")

    # Instance type checks
    if isinstance(sup, Human):
        print("I am human")
    if type(sup) is Superhero:
        print("I am a superhero")

    # Get the Method Resolution search Order used by both getattr() and super()
    # This attribute is dynamic and can be updated
    print(Superhero.__mro__)  # Prints "(<class '__main__.Superhero'>,
    # <class 'human.Human'>, <class 'object'>)"

    # Calls parent method but uses its own class attribute
    print(sup.get_species())  # Prints "Superhuman"

    # Calls overridden method
    print(sup.greet())  # Prints "HEY, Flash"

    # Calls method from Human
    sup.say("Spoon")  # Prints "Flash: Spoon"

    # Call method that exists only in Superhero
    sup.boast()  # Prints "I wield the power of super strength!"
    # Prints "I wield the power of bulletproofing!"

    # Inherited class attribute
    sup.age = 31
    print(sup.age)  # Returns 31

    # Attribute that only exists within Superhero
    print("Am I Oscar eligible? " + str(sup.movie))


#! Multiple Inheritance
# Batman inherits from both Superhero and Bat classes
if __name__ == "__main__":
    sup = Batman()

    # Get the Method Resolution search Order used by both getattr() and super().
    # This attribute is dynamic and can be updated
    print(Batman.__mro__)  # Prints "(<class '__main__.Batman'>,
    # <class 'superhero.Superhero'>,
    # <class 'human.Human'>,
    # <class 'bat.Bat'>, <class 'object'>)"

    # Calls parent method but uses its own class attribute
    print(sup.get_species())  # Prints "Superhuman"

    # Calls overridden method
    print(sup.greet())  # Prints "I'M BATMAN!"

    # Calls method from Human, because inheritance order matters
    sup.say("I agree")  # Returns Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    print(sup.sonar())  # Prints "))) ... (((""

    # Inherited class attribute
    sup.age = 100
    print(sup.age)  # Prints "100"

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print("Can I fly? " + str(sup.fly))  # Returns Can I fly? False
