import sys
from .commands import *

def main():
    args = sys.argv[1:]

    if not args: default(args)
    elif args[0] == 'argue': report_arguments(args)
    elif args[0] == 'task': do_tasks(args)
    elif args[0] == 'name': read_name(args)
    else: default(args)

if __name__ == '__main__':
    main()
