"""Define commands that the end user will call with the cli."""

from fletch_tools.good_input import get_input
from fletch_tools.progress_bar import print_progress

from .function_module import my_function
from .class_module import MyClass

# ----------------------------- #
#          Help Example         #
# ----------------------------- #

def show_help(cmds):
    """Show this help. then exit."""
    print('fletch_cli commands:')
    for i in cmds:
        print(15 * '-')
        print(i[0] + ':')
        print(i[1].__doc__)
    print(15 * '-')

# ----------------------------- #
#       Arguments Example       #
# ----------------------------- #

def report_arguments(args):
    """Show info about the arguments that were provided"""
    print('You supplied {} arguments.'.format(len(args)))

    if args:
        print('They were: ')
        for arg in args:
            print('Passed argument: {}'.format(arg))

# ----------------------------- #
#         Class Example         #
# ----------------------------- #

def read_name(args):
    """Show a progress bar example that "reads" a provided name."""
    print("Here is a progress bar example:")

    name = get_input('What is your name?', 'String')
    my_object = MyClass(name)
    my_object.read_name(print_progress)
    my_object.say_name()

# ----------------------------- #
#      Progress Bar Example     #
# ----------------------------- #

def do_tasks(args):
    """Show a progress bar example with the provided number of tasks to sim."""
    print("Here is a progress bar example:")
    qty = get_input('How many tasks should I simulate?', 'int')

    # A List of Items
    items = list(range(0, qty))
    items_len = len(items)

    # Initial call to print 0% progress
    print_progress(0, items_len)

    for i, item in enumerate(items):

        # Do stuff...
        my_function()

        # Update Progress Bar
        print_progress(i, items_len)
