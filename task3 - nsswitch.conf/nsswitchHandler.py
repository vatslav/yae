__author__ = 'django'
import re
inputFile = open('input.txt','r')
outFile = open('output.txt','w')
for line in inputFile:
    if line[0:5]=='hosts':
        line = line.replace('dns', '')
        N = 0
        for n in range(6,len(line[6:])):
            if line[n].isspace():
                N = n
            else:
                break
        line = line[:N] + 'dns' + line[N:]
    outFile.write(line)

inputFile.close()
outFile.close()

