__author__ = 'django'
import re

class mtrHandler(object):

    @staticmethod
    def analisys( ):

        return


class IOManager(object):
    def __init__(self):
        inputfile = open('input.txt', "r")
        outfile = open('output.txt', "w")
        mtr = [line for line in inputfile]
        out = mtrHandler.analisys(mtr)

        print(out)
        outfile.write(str(out))

        inputfile.close()
        outfile.close()
