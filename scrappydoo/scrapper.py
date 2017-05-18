class Collector(object):
    def __init__(self, name, repeat, interval):
        self.name = name
        self.repeat = repeat
        self.interval = interval

class Parser(object):
    def __init__(self, name):
        self.name = name
