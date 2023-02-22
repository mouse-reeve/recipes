""" Creates a recipe markdown file """
import json
import sys

from jinja2 import Template

if __name__ == "__main__":
    recipe = json.load(open(sys.argv[1]))
    output_format = sys.argv[2] if len(sys.argv) > 2 else "md"
    template = Template(open(f"template.{output_format}").read())
    print(template.render(recipe=recipe))
