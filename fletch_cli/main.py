import sys
from .commands import *

def main():
    args = sys.argv[1:]
    cmds = [
            ('help', show_help),
            ('argue', report_arguments),
            ('task', do_tasks),
            ('name', read_name)
           ]

    if not args or args[0] == 'help':
        show_help(cmds)
    else:
        for cmd in cmds:
            if args[0] == cmd[0]:
                cmd[1](args)              

if __name__ == '__main__':
    main()
