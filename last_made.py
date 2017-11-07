''' Keep track of when a recipe is made '''
from datetime import datetime
import json
import sys

def annotate(filename):
    ''' mark the recipe as made '''
    recipe_json = json.load(open(filename))
    date = datetime.now().isoformat()
    if not 'made' in recipe_json:
        recipe_json['made'] = []
    recipe_json['made'].append(date)

    return json.dumps(recipe_json)


if __name__ == '__main__':
    # user adds json filename of recipe
    recipe = sys.argv[1]
    print annotate(recipe)
