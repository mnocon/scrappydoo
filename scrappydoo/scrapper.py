class Scrapper(object):
    def __init__(self, name, collectorParams, parserParams):
        self.name = name
        self.collectorParams = collectorParams
        self.parserParams = parserParams

class CollectorParams(object):
    def __init__(self, repeat, interval):
        self.repeat = repeat
        self.interval = interval

class ParserParams(object):
    def __init__(self):
