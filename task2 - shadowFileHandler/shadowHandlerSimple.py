__author__ = 'vatslav'
inputfile = open('input.txt', "r")
count = 0
for line in inputfile:
    sep = line.find(':')
    if sep!=-1 and line[sep+1]!='*' and line[sep+1]!='!':
        count +=1

outfile = open('output.txt', "w")
outfile.write(str(count))