import configParser
from UrlCollector import UrlCollector
from threading import Event

if __name__ == "__main__":
    scrappers = configParser.parse_config()
    stopFlags = dict()
    for scrapper in scrappers:
        stopFlag = Event()
        stopFlags[scrapper.name] = stopFlag
        thread = UrlCollector(stopFlag, scrapper)
        thread.start()