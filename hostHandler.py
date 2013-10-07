__author__ = 'vatslav'
import re
import pprint


class HostHandler(object):
    host = []
    out = []

    @staticmethod
    def fixDomain_(hosts, sourceMashin, sourceDomain, replMashin, replDomain ):
        t = re.compile(r'(?<=\s)({0}[.]{1})+'.format(sourceMashin,sourceDomain))
        n = 0
        tempOut = []
        for host in hosts:
            host, n = re.subn(t,'{0}.{1}'.format(replMashin,replDomain), host)
            if n>0:
                host = re.sub(r'(?<=\s)({0})'.format(sourceMashin),'{0}'.format(replMashin),host)
            tempOut.append(host)

        out = ''.join(line for line in tempOut)
        return out


class IOManager(object):
    sourceMashin = 'bar'
    sourceDomain = 'domain.tld'
    replMashin = 'baz'
    replDomain =  'donemain.tld'
    def __init__(self):
        inputfile = open('input.txt', "r")
        outfile = open('output.txt', "w")
        hots = [line for line in inputfile]
        out = HostHandler.fixDomain_(hots, self.sourceMashin,self.sourceDomain,self.replMashin,self.replDomain)
        for line in out:
            outfile.write(line)


iomanager = IOManager()
