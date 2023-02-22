""" Creates a recipe markdown file """
import argparse
import glob
import json
import os
import re
import sys

from jinja2 import Template


def get_output_path(input_path, output_format):
    """Re-compose the url for the output"""
    dir_name = {"md": "markdown", "html": "html"}
    output_dir = re.sub(r"^json", dir_name[output_format], os.path.dirname(input_path))
    output_name = re.sub(r"json$", output_format, os.path.basename(input_path))
    return os.path.join(output_dir, output_name)


def write_file(input_path, output_path, output_format):
    """Load a recipe json file and write it to the corresponding output dir"""
    # Load the json file
    with open(input_path, "r", encoding="utf-8") as json_file:
        recipe_data = json.load(json_file)

    # Compile the Jinja template
    with open(f"template.{output_format}", "r", encoding="utf-8") as json_file:
        template = Template(json_file.read())

    # Write the output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(template.render(recipe=recipe_data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Format Recipe File",
        description="Creates a recipe file in a given format",
    )

    parser.add_argument("-a", "--all", action="store_true")
    parser.add_argument("-f", "--filename", action="store")
    format_choices = ["md", "html"]
    parser.add_argument("-o", "--output_format", choices=format_choices)

    args = parser.parse_args()

    compile_all = args.all
    filename = args.filename
    format_preference = args.output_format

    if not compile_all and not filename:
        sys.stderr.write("Filename must be provided with -f if -a flag is not used\n")
        sys.exit()

    files = glob.glob("json/**/*.json") if compile_all else [filename]
    formats = [format_preference] if format_preference else format_choices

    # either get all the files or one specific file
    sys.stdout.write(f"Writing {len(files)} file(s):\n")
    for file in files:
        for version in formats:
            sys.stdout.write('.')
            output_filename = get_output_path(file, version)
            write_file(file, output_filename, version)
    sys.stdout.write("\n")
