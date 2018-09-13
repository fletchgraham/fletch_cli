import sys
from .good_input import get_input
from .progress_bar import progressBar

from .class_module import MyClass
from .function_module import my_function

def main():
    print('Welcome!')

    # ----------------------------- #
    #       Arguments Example       #
    # ----------------------------- #

    args = sys.argv[1:]

    print('Number of arguments: {}'.format(len(args)))
    print('Arguments: ')

    for arg in args:
        print('Passed argument: {}'.format(arg))

    # ----------------------------- #
    #         Class Example         #
    # ----------------------------- #

    my_object = MyClass('Fletcher')
    my_object.say_name()

    # ----------------------------- #
    #      Progress Bar Example     #
    # ----------------------------- #

    qty = get_input('How many items?', 'int')

    # A List of Items
    items = list(range(0, qty))

    # Initial call to print 0% progress
    pbar = progressBar(len(items))
    pbar.print_bar(0)

    for i, item in enumerate(items):

        # Do stuff...
        my_function()

        # Update Progress Bar
        pbar.print_bar(i + 1)

if __name__ == '__main__':
    main()
