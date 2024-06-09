
MAX_VALUE_ADC = 16383 # 14 bits, 0x3fff
class graphInterval:
    def __init__(self, interval, startTime, samples):
        self.intervalNo = interval     # intervals numbered 1, ...
        self.startTime = startTime     # ux time start
        self.samples = samples         # number of samples
        graphX = []                    # the x-axis result list
        graphY = []                    # the y-axis result list
class graph:
    def __init__(self, inFile, intervals, samples, outFile):
        self.inFile = inFile           # sample log file name and path
        self.intervals = intervals     # number of intervals
        self.samples = samples         # total nuber of samples
        self.outFile = outFile         # Some kind of outfile
    def content(self):
        print(self.inFile, self.intervals, self.samples, self.outFile)

from matplotlib import pyplot as plt
import numpy as np
import datetime

with open("SMPLOG3_240523.txt") as datasource:
    rawData = datasource.readlines()

print("Length of raw data is : " + str(len(rawData)) + " elements")


# Extract timestamps
timeStamps = []
for i in range(len(rawData)):
    val = int(rawData[i])
    if val > MAX_VALUE_ADC:
        timeStamps.append(val)

# Extract samples
sampleCnt = []
samples = 0
for i in range(len(rawData)-1):
    val = int(rawData[i+1])
    if val <= MAX_VALUE_ADC:
        samples += 1
    else:
        sampleCnt.append(samples)
        samples = 0
sampleCnt.append(samples)

# Check the sum of elements are correct, Sum of raw data elements - number of timestamps = sum of samplsCnt

if (len(rawData) - len(timeStamps) != sum(sampleCnt)):
    print('Error in element handling!')

# Create Graph object
graph = graph('SMPLOG3_240523.txt', len(timeStamps), sum(sampleCnt), "outFileName.txt")
graph.content() # prints content of graph object

# Create interval objects
intervalList = []
for i in range(len(timeStamps)):
    intervalList.append(graphInterval(i+1, timeStamps[i], sampleCnt[i]))

for i in range(len(intervalList)):
    print(intervalList[i].intervalNo, intervalList[i].samples, intervalList[i].startTime)
