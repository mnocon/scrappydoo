import json
import validictory
from scrapper import Scrapper

def parse_config():
    with open('scrappydoo\config.json', 'r') as f:
        data = json.load(f)
    with open('scrappydoo\configSchema.json', 'r') as f:
        schema = json.load(f)   
    validate(data, schema)
    scrappies = list()
    for scrapperData in data['scrappies']:
        yield Scrapper(scrapperData['name'], scrapperData['collectorParams']['interval'])

def validate(data, schema):
    validictory.validate(data, schema)
    names = list()
    for scrappy in data['scrappies']:
        names.append(scrappy['name'])
 
    assert(len(names) == len(set(names)))