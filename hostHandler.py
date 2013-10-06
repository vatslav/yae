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
        output = []
        #buf = set(line in self.f)
        #self.print()
        self.handler()
        #self.printer()

    def printer(self):
        print(self.hosts)

    @staticmethod
    def __fixDomain_(m):
        return ''


    def handler(self):
        #p = re.compile(r'(\sbar[.]domain[.]tld)')
        t = re.compile(r'(\s[bar.domain.tld]+)')
        t = re.compile('(?P<ip>[\d+.\d+.\d+.\d+]+) | (?P<domain>\w+)')
        result = re.finditer(t,self.hosts)
        for math  in result:
            print(math.group())
        #self.hosts=re.sub(p,'\tbaz.donemain.tld', self.hosts)
        #p = re.compile(r'\sbaz.doneain.tld .')
        #self.hosts = p.sub()




d = HostHandler(file)


