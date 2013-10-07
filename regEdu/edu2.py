__author__ = 'django'
import re
#p = re.compile(r'(\sbar[.]domain[.]tld)')
#t = re.compile('(?P<ip>[\d+.\d+.\d+.\d+]+) | (?P<domain>\w+)')

        #self.out = re.sub(t, '\tbaz.donemain.tld', self.hosts)
        #self.hosts = re.sub(t2,'\tbaz',self.hosts)

        #self.hosts=re.sub(p,'\tbaz.donemain.tld', self.hosts)
        #p = re.compile(r'\sbaz.doneain.tld .')
        #self.hosts = p.sub()

#hosts = [line for line in file]
#output = []
domainSeach = 'domain.tld'
domainRepl = 'donemain.tld'
mashinSeash = 'bar'
mashinRepl = 'baz'

string = '333334 333 123 2334 33345 54443 2195433333332 123333333 44444'
pattern = '[\d]*(?<!3)3{2,4}(?!3)[\d]*'
#print(re.findall(pattern, string))
string = '''333334 333 123 2334 33345 54443 2195433333332
123333333 44444 will ponn'''
#print(string[:])
