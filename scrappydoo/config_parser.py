"""test"""

import json
import validictory
from scrapper import Scrapper
from scrapper import CollectorParams
from scrapper import ParserParams

class ConfigParser(object):
    def __init__(self, config_path, config_schema_path):
        self.config_path = config_path
        self.config_schema_path = config_schema_path

    def parse_config(self, config_path, config_schema_path):
        with open(config_path, 'r') as f:
            data = json.load(f)
        with open(config_schema_path, 'r') as f:
            schema = json.load(f)
        validate(data, schema)
        for scrapper_data in data['scrappies']:
            collector_params = CollectorParams(
                scrapper_data['collectorParams']['interval'],
                scrapper_data['collectorParams']['interval'])
            yield Scrapper(scrapper_data['name'], collector_params)

    def validate(self, data, schema):
        validictory.validate(data, schema)
        names = list()
        for scrappy in data['scrappies']:
            names.append(scrappy['name'])

        assert(len(names) == len(set(names))
