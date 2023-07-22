# superhero.py
from superhero import Superhero
from bat import Bat


# Define Batman as a child that inherits from both Superhero and Bat
class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".
        Superhero.__init__(
            self, "anonymous", movie=True, superpowers=["Wealthy"], *args, **kwargs
        )
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = "Sad Affleck"

    def greet(self, loud=False):
        if loud:
            print("I'M BATMAN!")
        else:
            print("I'm batman!")
