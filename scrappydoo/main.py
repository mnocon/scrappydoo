from threading import Event
import config_parser
from url_collector import UrlCollector

COLLECTORS_FILE = """.\\scrappydoo\\collectors.json"""
COLLECTORS_SCHEMA_FILE = """.\\scrappydoo\\collectorsSchema.json"""

def main():
    stop_flags = dict()
    for collector in config_parser.parse_collectors(COLLECTORS_FILE, COLLECTORS_SCHEMA_FILE):
        stop_flag = Event()
        stop_flags[collector.name] = stop_flag
        thread = UrlCollector(stop_flag, collector)
        thread.start()

if __name__ == "__main__":
    main()
