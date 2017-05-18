"""
Created on 29 July 2012
@author: Lisa Simpson
"""

from threading import Event
import config_parser
from UrlCollector import UrlCollector

if __name__ == "__main__":
    main()

def main():
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    scrappers = ConfigParser.parse_config()
    stop_flags = dict()
    for scrapper in scrappers:
        stop_flag = Event()
        stop_flags[scrapper.name] = stop_flag
        thread = UrlCollector(stop_flag, scrapper)
        thread.start()