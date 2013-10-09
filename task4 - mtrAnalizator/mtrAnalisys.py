__author__ = 'vatsav'
import re
import functools
from functools import reduce
from copy import deepcopy,copy

@functools.total_ordering
class MtrStruct(object):
    def __init__(self,n, ip, loss, snt, last, avg, best, wrst, stdev):
        core = []
        self.n=int(n)
        self.ip = ip
        self.loss = float(loss)
        self.snt = int(snt)
        self.last = float(last)
        self.avg = float(avg)
        self.best=float(best)
        self.wrst=float(wrst)
        self.stdev=float(stdev)

    def __gt__(self, other): #>
        if self.loss>other.loss: return 1
        if self.loss<other.loss: return 0
        if self.loss==other.loss:
            if self.stdev>other.stdev:return 1
            if self.stdev<other.stdev:return 0
            if self.stdev==other.stdev:
                if self.avg>other.avg: return 1
                else: return 0

    def __eq__(self, other):
        if self.loss==other.loss:
            if self.stdev==other.stdev:
                if self.avg==other.avg: return 1
        return  0

    def __copy__(self, memodict={}):
        t = MtrStruct(self.n, self.ip, self.loss, self.snt, self.last, self.avg, self.best, self.wrst, self.stdev)
        return t

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.n,self.loss,self.stdev, self.avg)

#HOST: pooh                       Loss%   Snt   Last   Avg  Best  Wrst StDev
#  1.|-- 84.201.169.254             0.0%     9    1.3   1.3   1.0   2.4   0.5
#  2.|-- 37.9.74.134                0.0%     9    1.6  18.4   1.2 121.4  39.8
class MtrHandler(object):
    @staticmethod
    def rawDataHandler(mtr):
        mtrStorage = []
        template = re.compile(r'\s*(?P<n>\d+)\s*\.\s*[|]{1}\s*-\s*-\s+(?P<ip>\S+)\s+(?P<loss>\d+\.?\d*)%?\s+(?P<snt>\d+)\s+(?P<last>\d+\.?\d*)\s+(?P<avg>\d+\.?\d*)\s+(?P<best>\d+\.?\d*)\s+(?P<wrst>\d+\.?\d*)\s+(?P<stdev>\d+\.?\d*).*')
        for line in mtr:
            m = re.search(template,line)
            if m!=None:
                mtrStorage.append(MtrStruct(m.group('n'),m.group('ip'),m.group('loss'),m.group('snt'),m.group('last'),m.group('avg'),m.group('best'),m.group('wrst'),m.group('stdev')))

        return mtrStorage

    @staticmethod
    def analisys(mtr):
        storage = MtrHandler.rawDataHandler(mtr)
        if len(storage)>0:
            return max(storage).n
        else:

            return 1


class IOManager(object):
    def __init__(self):
        inputfile = open('input.txt', "r")

        mtr = [line.rstrip() for line in inputfile]
        out = MtrHandler.analisys(mtr)
        if out!=-1:
            outfile = open('output.txt', "w")
            outfile.write(str(out))
            outfile.close()
        inputfile.close()


iomanger = IOManager()