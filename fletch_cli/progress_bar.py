# Print iterations progress

class progressBar:

    def __init__(self,
                 total,
                 prefix='Progress:',
                 suffix='Complete',
                 decimals=1,
                 length=50,
                 fill='|'
                 ):

        self.iteration = 0
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill

    def print_bar(self, iteration):

        self.iteration = iteration

        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (self.iteration / float(self.total)))
        filledLength = int(self.length * self.iteration // self.total)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)

        print('\r%s |%s| %s%% %s' % (self.prefix, bar, percent, self.suffix), end = '\r')

        # Print New Line on Complete
        if self.iteration == self.total:
            print()
