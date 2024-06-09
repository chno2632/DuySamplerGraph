MAX_VALUE_ADC = 16383 # 14 bits, 0x3fff
class graphInterval:
    def __init__(self, interval, startTime, samples):
        self.intervalNo = interval     # intervals numbered 1, ...
        self.startTime = startTime     # ux time start
        self.samples = samples         # number of samples
        graphX = []                    # the x-axis result list
        graphY = []                    # the y-axis result list


class graph:
    def __init__(self, inFile, intervals, outFile):
        inFile = self.inFile           # sample log file name and path
        intervals = self.intervals     # number of intervals
        outFile = self.outFile


from matplotlib import pyplot as plt
import numpy as np
import datetime

with open("SMPLOG3_240523.txt") as datasource:
    rawData = datasource.readlines()
