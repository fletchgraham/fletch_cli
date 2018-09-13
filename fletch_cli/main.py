import sys
from .good_input import get_input
from .progress_bar import print_progress

from .class_module import MyClass
from .function_module import my_function

def main():
    print('Welcome.')
    get_input('Press enter to see some examples, or ctrl+C to quit.', 'enter')

    # ----------------------------- #
    #       Arguments Example       #
    # ----------------------------- #

    args = sys.argv[1:]

    print('You supplied {} arguments.'.format(len(args)))

    if args:
        print('They were: ')
        for arg in args:
            print('Passed argument: {}'.format(arg))

    # ----------------------------- #
    #         Class Example         #
    # ----------------------------- #

    name = get_input('What is your name?', 'String')
    my_object = MyClass(name)
    my_object.read_name(print_progress)
    my_object.say_name()

    # ----------------------------- #
    #      Progress Bar Example     #
    # ----------------------------- #

    print("Here is another progress bar example.")
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

    get_input("Now dig in and turn this into a useful CLI!", 'enter')

if __name__ == '__main__':
    main()
