__author__ = 'django'
import re

log='''64 bytes from localhost.localdomain (127.0.0.1): icmp_req=1 ttl=64 time=0.033 ms
64 bytes from localhost.localdomain (127.0.0.1): icmp_req=2 ttl=64 time=0.034 ms
64 bytes from localhost.localdomain (127.0.0.1): icmp_req=3 ttl=64 time=0.031 ms
64 bytes from localhost.localdomain (127.0.0.1): icmp_req=4 ttl=64 time=0.031 ms'''
pattern = re.compile('icmp_req=[\d]+ .* (time=[\d]+[.]?[\d]+ ms)')
m = re.finditer(pattern, log)
result = []
for x in m:
    result.append(x.groups())
#print(result)

class A(object):
    b=2
    def __init__(self):
        pass

a = A()
A.b=5
print(A.b)