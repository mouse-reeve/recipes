''' Creates a recipe markdown file '''
import json
import sys

def format_markdown(recipe_json):
    ''' Produces a mardown file for a recipe '''
    recipe_json = json.loads(recipe_json)
    if not 'ingredients' in recipe_json:
        return

    print '%s' % recipe_json['title']
    print '=' * len(recipe_json['title'])

    print recipe_json.get('notes', '')

    if 'quantity' in recipe_json:
        print '**Makes**: %s' % recipe_json['quantity']

    print ''
    print '### Ingredients'
    for item in recipe_json['ingredients']:
        if isinstance(item, dict):
            title = item.keys()[0]
            print '- %s:' % title
            for i in item[title]:
                print '    - %s' % format_ingredient(i)
        else:
            print '- %s' % format_ingredient(item)
    print ''

    if 'steps' in recipe_json:
        print '### Steps'
        for item in recipe_json['steps']:
            if isinstance(item, dict):
                title = item.keys()[0]
                print '%s:' % title
                for i in item[title]:
                    print '- %s' % i
            else:
                print item
            print ''

    if 'source' in recipe_json:
        print '> Source: %s' % recipe_json['source']

def format_ingredient(ingredient):
    ''' clean up the ingredient highlighting syntax '''
    return ingredient.replace(r'{', '').replace(r'}', '')

if __name__ == '__main__':
    format_markdown(sys.argv[1])
