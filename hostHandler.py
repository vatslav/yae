__author__ = 'vatslav'
import re
import pprint
file = open('input.txt', "r")
#hosts = [line for line in file]
#output = []
domainSeach = 'domain.tld'
domainRepl = 'donemain.tld'
mashinSeash = 'bar'
mashinRepl = 'baz'


class HostHandler(object):
    def __init__(self, f):
        self.f=f

        self.hosts = ''.join(line for line in self.f)
        #self.hosts = [line for line in self.f]
        output = []
        #buf = set(line in self.f)
        #self.print()
        self.handler()
        #self.printer()

    def printer(self):
        print(self.out)
        print(self.hosts)

    @staticmethod
    def __fixDomain_(m):
        return ''

#t = re.compile('(?P<ip>[\d+.\d+.\d+.\d+]+) | (?P<domain>\w+)')
    def handler(self):
        #p = re.compile(r'(\sbar[.]domain[.]tld)')
        t = re.compile(r'(bar[.]domain[.]tld)+')
        t2 = re.compile(r'\s[bar]{1}')
        for m in re.finditer(t,self.hosts):
            print(m.group())
            print(m.end())
            print(self.hosts[m.start():m.end()])
        self.out = re.sub(t, '\tbaz.donemain.tld', self.hosts)
        #self.hosts = re.sub(t2,'\tbaz',self.hosts)

        #self.hosts=re.sub(p,'\tbaz.donemain.tld', self.hosts)
        #p = re.compile(r'\sbaz.doneain.tld .')
        #self.hosts = p.sub()




d = HostHandler(file)


