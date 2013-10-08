__author__ = 'django'
from copy import copy
class T(object):
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if self.a==other.a:return 1
        else: return -1
    def __lt__(self, other):
        return self.a<other.a
    def __gt__(self, other):
        return self.a>other.a
    def __str__(self):
        return str(self.a)
    def __copy__(self):
        return T(self.a)

a = T(2)
b = copy(a)
a.a=5
print(b)