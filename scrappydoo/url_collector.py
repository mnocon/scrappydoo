import sqlite3
from threading import Thread
from scrapper import Collector

class UrlCollector(Thread):
    collector_interval = 5

    def __init__(self, event, collector):
        Thread.__init__(self)
        self.stopped = event
        self.collector = collector

    def __initialize():
        pass
        # pobierz wszystkie z bazy - zrob union, grupy: obecne w db, obecne w configu, i tu i tu
        # 

        # obecne w db i w obu (z overwrite): ustaw disabled
        # obecne w configu: dodaj nowy collector
        #obecne w configu i w obu (z overwrite): dodaj nowy rekord

        #run:
        #    uruchom
        #
        #    oznacz date wykonania i blad
        #    dodaj wpis z kolejnym uruchomieniem

        #sprawdz czy jest w bazie
        #jesli tak i flaga overwrite: ustaw istniejace pola na null, wstaw nowy rekord do przetworzenia
        #jesli tak i flaga ovwewrite false: nie rob nic
        # jesli nie: wstaw collector, wstaw nowy rekord

    def run(self):
        while not self.stopped.wait(self.collector_interval):
            if not self.is_scheduled_for_run():
                return

            self.__process()

            if not self.collector.repeat:
                self.stop()

    def __process(self):
        print(self.collector.name)

    def stop(self):
        self.stopped.set()

    def is_scheduled_for_run(self):
        # get data from db
        return True
            