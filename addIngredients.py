''' ingest all ingredients from a plaintext list '''
import os
import json
from py2neo import authenticate, Graph
import re
import sys

user = os.environ['NEO4J_USER']
password = os.environ['NEO4J_PASS']
authenticate('localhost:7474', user, password)
graph = Graph()

def add_items(json_file_path):
    ''' add nodes based on scraped json '''
    with open(json_file_path) as data_file:
        data = json.load(data_file)

        ingredients = [i for i in data['ingredients'] if '{' in i]
        ingredients = [re.sub(r'.*\{(.*)\}.*', r'\1', i) for i in ingredients]

        for ingredient in ingredients:
            query = 'MATCH (n:ingredient {identifier: "%s"}) ' \
                    'RETURN n' % ingredient
            result = graph.cypher.execute(query)
            if len(result.records):
                continue

            print 'adding %s' % ingredient
            query = 'CREATE (n:ingredient {identifier: "%s"}) ' \
                    'RETURN n' % ingredient
            graph.cypher.execute(query)

if __name__ == '__main__':
    add_items(sys.argv[1])
