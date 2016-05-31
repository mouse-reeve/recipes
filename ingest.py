''' ingest a recipe and its ingredients '''
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
        recipe_node = {
            'identifier': data['title'],
            'content': json.dumps(data)
        }

        ingredients = [i for i in data['ingredients'] if '{' in i]
        ingredients = [re.sub(r'.*\{(.*)\}.*', r'\1', i) for i in ingredients]

        if not len(ingredients):
            print 'NO INGREDIENTS FOUND: %s' % data['title']
            return

        # this assumes that all the ingredient nodes already exist
        ingredient_match = []
        ingredient_where = []
        ingredient_create = []
        for (index, ingredient) in enumerate(ingredients):
            ingredient_match.append('(n%d:ingredient)' % index)
            ingredient_where.append('n%d.identifier = \"%s\"' % (index, ingredient))
            ingredient_create.append('CREATE n-[:uses]->n%d' % index)

        query = 'MATCH ' + ', '.join(ingredient_match) + ' '
        query += 'WHERE ' + ' AND '.join(ingredient_where) + ' '
        query += 'CREATE (n:recipe {recipe}) ' + \
                ' '.join(ingredient_create) + \
                ' RETURN n'

        print 'Adding recipe: %s' % data['title']
        result = graph.cypher.execute(query, recipe=recipe_node)
        if not len(result.records):
            print 'ERROR ADDING: %s' % data['title']

if __name__ == '__main__':
    add_items(sys.argv[1])
