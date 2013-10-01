__author__ = 'vatslav'
file = open('input.txt', "r")


class HostHandler:
    def __init__(self, f):
        self.f=f

        self.hosts = [line for line in self.f]
        #buf = set(line in self.f)
        print(self.hosts,type(self.hosts))


hostHandler = HostHandler(file)
