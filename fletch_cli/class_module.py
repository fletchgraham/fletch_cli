"""Example module with a class."""
from time import sleep

class MyClass():
    """Demonstrate using a class with the cli."""
    def __init__(self, name):
        self.name = str(name)

    def read_name(self, progress_report):
        """Sleep on each letter of the name.
        An example to show how the progress bar can be used on a class method.
        """
        name_len = len(self.name)
        print('Reading name. Please wait.')
        for i, letter in enumerate(self.name):
            sleep(0.2)
            progress_report(i, name_len)

    def say_name(self):
        """Display name."""
        print('Your name is {}.'.format(self.name))
