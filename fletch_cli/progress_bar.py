"""A simple cli progress bar"""

def print_progress(iteration, total):
    """Print a progress bar showing a given level of completion."""
    iteration += 1
    prefix = 'Progress'
    suffix = 'Complete'
    length = 50
    fill = '|'

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)

    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

    # Print New Line on Complete
    if iteration == total:
        print()
