import struct

__author__ = 'django'
import re
class MtrStruct(object):
    def __init__(self,n, ip, loss, snt, last, avg, best, wrst, stdev):
        self.n=n
        self.ip = ip
        self.loss = loss
        self.snt = snt
        self.last = last
        self.avg = avg
        self.best=best
        self.wrst=wrst
        self.stdev=stdev

#HOST: pooh                        Loss%   Snt   Last   Avg  Best  Wrst StDev
#  1.|-- 84.201.169.254             0.0%     9    1.3   1.3   1.0   2.4   0.5
#  2.|-- 37.9.74.134                0.0%     9    1.6  18.4   1.2 121.4  39.8
#(?P<n>\d{1})\.[|]{1}--\s+(?P<ip>(\d{1,3}\.){3}\d{1,3})\s+(?P<loss>\d{1,2}\.\d+%)\s+(?P<cnt>\d+)\s+(?P<last>\d+\.\d+)\s+(?P<avg>\d+\.\d+)\s+(?P<best>\d+\.\d+)\s+(?P<wrst>\d+\.\d+)\s+(?P<stdev>\d+\.\d+)
class mtrHandler(object):
    @staticmethod
    def rawDataHandler(mtr):
        mtrStorage = []
        template = re.compile(r'(?P<n>\d{1})\.[|]{1}--\s+(?P<ip>(\d{1,3}\.){3}\d{1,3})\s+(?P<loss>\d{1,2}\.\d+%)\s+(?P<cnt>\d+)\s+(?P<last>\d+\.\d+)\s+(?P<avg>\d+\.\d+)\s+(?P<best>\d+\.\d+)\s+(?P<wrst>\d+\.\d+)\s+(?P<stdev>\d+\.\d+)')
        for line in mtr:
            m = re.match(template,line)
            if m!=None:
                mtrStorage.append(MtrStruct(m.group('n'),m.group('ip'),m.group('loss'),m.group('snt'),m.group('last'),m.group('avg'),m.group('best'),m.group('wrst'),m.group('stdev')))

        return mtrStorage

    @staticmethod
    def analisys(mtr):
        storage = mtrHandler.rawDataHandler(mtr)





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
