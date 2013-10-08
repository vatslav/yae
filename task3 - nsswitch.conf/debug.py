__author__ = 'django'
import re
s = 'hosts:      myhostname files mdns4_minimal [NOTFOUND=return] dns myhostname'
a = re.findall(r'my',s) is None
print(str(a))