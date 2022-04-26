""" Creates a recipe markdown file """
import json
import sys

from jinja2 import Template

if __name__ == "__main__":
    recipe = json.load(open(sys.argv[1]))
    try:
        template = Template(open(sys.argv[2]).read())
    except (TypeError, IndexError):
        template = Template(open("template.md").read())
    print(template.render(recipe=recipe))
