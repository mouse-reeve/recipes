""" Creates a recipe markdown file """
import argparse
import json
import os
import re

from jinja2 import Template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Format Recipe File",
        description="Creates a recipe file in a given format",
    )

    parser.add_argument("filename", action="store", type=str)
    parser.add_argument(
        "-f", "--format", choices=["md", "html"], required=True, type=str
    )

    args = parser.parse_args()
    filename = args.filename
    file_format = args.format

    with open(filename, "r", encoding="utf-8") as json_file:
        recipe_data = json.load(json_file)

    with open(f"template.{file_format}", "r", encoding="utf-8") as json_file:
        template = Template(json_file.read())

    dir_name = {"md": "markdown", "html": "html"}
    output_dir = re.sub(r"^json", dir_name[file_format], os.path.dirname(filename))
    output_name = re.sub(r"json$", file_format, os.path.basename(filename))
    output_filename = os.path.join(output_dir, output_name)

    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write(template.render(recipe=recipe_data))
