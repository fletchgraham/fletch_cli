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
    """fletch argue [args]
    Show info about suppied args.
    """
    print('You supplied {} arguments.'.format(len(args)))

    if args:
        print('They were: ')
        for arg in args:
            print('Passed argument: {}'.format(arg))

# ----------------------------- #
#         Class Example         #
# ----------------------------- #

def read_name(args):
    """fletch read [name]
    "Read" a provided name.
    """
    print("Here is a progress bar example:")

    name = get_input('What is your name?', 'String')
    my_object = MyClass(name)
    my_object.read_name(print_progress)
    my_object.say_name()

# ----------------------------- #
#      Progress Bar Example     #
# ----------------------------- #

def do_tasks(args):
    """fletch tasks [int]
    Simulate a given number of tasks.
    """
    
    print("I'll pretend to run through some tasks.")
    try:
        qty = int(args[1])
    except:
        qty = get_input('How many tasks should I simulate?', 'int')

    # A List of Tasks
    tasks = list(range(0, qty))
    tasks_len = len(tasks)

    for i, item in enumerate(tasks):

        # Do stuff...
        my_function()

        # Update Progress Bar
        print_progress(i, tasks_len)
