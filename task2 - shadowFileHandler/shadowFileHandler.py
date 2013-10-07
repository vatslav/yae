__author__ = 'django'
import re
class ShadowHandler(object):
    @staticmethod
    def userCount(shadowF):
        count = 0
        pattern = re.compile(r'\w+[:]([*])|([!])')
        for line in shadowF:
            if re.match(pattern,line):
                #print(line)
                count +=1

        return count

#35
class IOManager(object):
    Domain =  'donemain.tld'
    def __init__(self):
        inputfile = open('input.txt', "r")
        outfile = open('output.txt', "w")
        shadow = [line for line in inputfile]
        out = ShadowHandler.userCount(shadow)
        print(out)
        print(len(shadow))
        outfile.write(str(out))

iomanager = IOManager()