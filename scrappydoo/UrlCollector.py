from threading import Thread

class UrlCollector(Thread):
    def __init__(self, event, scrapper):
        Thread.__init__(self)
        self.stopped = event
        self.scrapper = scrapper

    def run(self):
        while not self.stopped.wait(self.scrapper.interval):
            print(self.scrapper.name)

            