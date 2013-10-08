__author__ = 'django'
import re
inputFile = open('input.txt','r')
outFile = open('output.txt','w')
dns = re.compile('\sdns\s')
files = re.compile('\sfiles\s')
for line in inputFile:
    if line[0:6]=='hosts:' and re.search(files,line) is not None and re.search(dns,line) is not None:
        if re.search(files,line).start()<re.search(dns,line).start():
            line = re.sub('(?<=\s)dns(?=\s)', "", line)
            N = 0
            for n in range(7,len(line[7:])):
                if line[n].isspace():
                    N = n
                else:
                    break
            line = line[:N+1] + 'dns' + line[N:]
    outFile.write(line)

inputFile.close()
outFile.close()

