"""test"""
import json
import validictory
from scrapper import Collector

def parse_collectors(config_path, config_schema_path):
    with open(config_path, 'r') as config_file:
        data = json.load(config_file)
    with open(config_schema_path, 'r') as config_schema_file:
        schema = json.load(config_schema_file)
    _validateCollectors(data, schema)
    for scrapper_data in data['collectors']:
        yield Collector(
            scrapper_data['name'],
            scrapper_data['repeat'],
            scrapper_data['interval'])

def _validateCollectors(data, schema):
    validictory.validate(data, schema)
    names = list()
    for collector in data['collectors']:
        names.append(collector['name'])
    assert(len(names) == len(set(names)))
