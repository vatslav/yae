__author__ = 'django'
import re
import functools
from functools import reduce

class MtrStruct(object):
    def __init__(self,n, ip, loss, snt, last, avg, best, wrst, stdev):
        self.n=int(n)
        self.ip = ip
        self.loss = float(loss)
        self.snt = int(snt)
        self.last = float(last)
        self.avg = float(avg)
        self.best=float(best)
        self.wrst=float(wrst)
        self.stdev=float(stdev)

#HOST: pooh                        Loss%   Snt   Last   Avg  Best  Wrst StDev
#  1.|-- 84.201.169.254             0.0%     9    1.3   1.3   1.0   2.4   0.5
#  2.|-- 37.9.74.134                0.0%     9    1.6  18.4   1.2 121.4  39.8
#(?P<n>\d{1})\.[|]{1}--\s+(?P<ip>(\d{1,3}\.){3}\d{1,3})\s+(?P<loss>\d{1,2}\.\d+%)\s+(?P<cnt>\d+)\s+(?P<last>\d+\.\d+)\s+(?P<avg>\d+\.\d+)\s+(?P<best>\d+\.\d+)\s+(?P<wrst>\d+\.\d+)\s+(?P<stdev>\d+\.\d+)
class MtrHandler(object):
    @staticmethod
    def rawDataHandler(mtr):
        mtrStorage = []
        template = re.compile(r'\s*(?P<n>\d{1})\.[|]{1}--\s+(?P<ip>(\d{1,3}\.){3}\d{1,3})\s+(?P<loss>\d{1,2}\.\d+)%\s+(?P<snt>\d+)\s+(?P<last>\d+\.\d+)\s+(?P<avg>\d+\.\d+)\s+(?P<best>\d+\.\d+)\s+(?P<wrst>\d+\.\d+)\s+(?P<stdev>\d+\.\d+).*')
        for line in mtr:
            print(line)
            m = re.match(template,line)
            if m!=None:
                mtrStorage.append(MtrStruct(m.group('n'),m.group('ip'),m.group('loss'),m.group('snt'),m.group('last'),m.group('avg'),m.group('best'),m.group('wrst'),m.group('stdev')))

        return mtrStorage

    @staticmethod
    def analisys(mtr):
        storage = MtrHandler.rawDataHandler(mtr)
        value = storage[0].loss
        n = 0
        for i in range(len(storage)):
            if storage[i].loss<value:
                value = storage[i].loss
                n = i

        return n


class IOManager(object):
    def __init__(self):
        inputfile = open('input.txt', "r")
        outfile = open('output.txt', "w")
        mtr = [line.rstrip() for line in inputfile]
        out = MtrHandler.analisys(mtr)

        print(out)
        outfile.write(str(out))

        inputfile.close()
        outfile.close()

iomanger = IOManager()