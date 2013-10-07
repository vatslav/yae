__author__ = 'vatslav'
import re
import pprint
file = open('input.txt', "r")



class HostHandler(object):
    def __init__(self, f):
        self.f=f
        self.hosts = [line for line in self.f]
        self.tempOut = []
        self.out=''

        self.handler()
        self.printer()

    def printer(self):
        print(self.out)

    @staticmethod
    def handlerStat( ):
        pass

    @staticmethod
    def fixDomain_(hosts, sourceMashin, sourceDomain, replMashin, replDomain ):
        t = re.compile('({0}[.]{1})+')
        n = 0
        for host in hosts:
            host, n = re.subn(t,'\tbaz.donemain.tld', host)
            if n>0:
                host = re.sub(r'\sbar','\tbaz',host)
            self.tempOut.append(host)


    def handler(self):
        t = re.compile('(bar[.]domain[.]tld)+')
        n = 0
        for host in self.hosts:
            host, n = re.subn(t,'\tbaz.donemain.tld', host)
            if n>0:
                host = re.sub(r'bar','\tbaz',host)
            self.tempOut.append(host)


        self.out = ''.join(line for line in self.tempOut)






d = HostHandler(file)

#print(HostHandler.fixDomain_(1))
