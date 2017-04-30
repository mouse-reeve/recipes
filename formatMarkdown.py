''' Creates a recipe markdown file '''
from jinja2 import Template
import json
import sys

if __name__ == '__main__':
    recipe = json.load(open(sys.argv[1]))
    template = Template(open('template.md').read())
    print template.render(recipe=recipe)
