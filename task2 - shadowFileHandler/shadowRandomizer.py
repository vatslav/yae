__author__ = 'django'
import random
inputfile = open('input.txt', "r")
outfile = open('output.txt', "w")
count = 0
for line in inputfile:
    sep = line.find(':')
    sep = line.find(':',sep+1)
    end = line.find(':',sep+1)
    line = line[:sep+1] + str(random.randint(1000,50000)) + line[end:]
    sep = line.find(':',sep+1)
    sep = line.find(':',sep+1)
    end = line.find(':',sep+1)
    line = line[:sep+1] + str(random.randint(1000,50000)) + line[end:]
    sep = line.find(':',sep+1)
    end = line.find(':',sep+1)
    line = line[:sep+1] + str(random.randint(3,11)) + line[end:]
    outfile.write(line)