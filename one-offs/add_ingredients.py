''' ingest all ingredients from a plaintext list '''
import os
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
        for line in data_file.readlines():
            ingredient = {'identifier': re.sub(r'\n', '', line)}

            query = 'CREATE (n:ingredient {ingredient})'
            graph.cypher.execute(query, ingredient=ingredient)

if __name__ == '__main__':
    add_items(sys.argv[1])

