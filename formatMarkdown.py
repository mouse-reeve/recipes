import json
import sys

def format_markdown(recipe_json):
    recipe_json = json.loads(recipe_json)
    if not 'ingredients' in recipe_json:
        return

    print '%s' % recipe_json['title']
    print '=' * len(recipe_json['title'])

    if 'notes' in recipe_json:
        print recipe_json['notes']
    print ''

    for item in recipe_json['ingredients']:
        print '- %s' % item
    print ''

    for item in recipe_json['steps']:
        print item
        print ''

    if 'source' in recipe_json:
        print '> Source: %s' % recipe_json['source']


if __name__ == '__main__':
    format_markdown(sys.argv[1])
