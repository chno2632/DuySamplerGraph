class graphInterval:
    def __init__(self, interval, startTime, samples):
    self.intervalNo = interval     # intervals numbered 1, ...
    self.startTime = startTime     # ux time start
    self.samples = samples         # number of samples
    graphX = []                    # the x-axis result list
    graphY =[]                     # the y-axis result list


class graph:
    inFile          # sample log file name and path
    intervals       # number of intervals
    outFile
