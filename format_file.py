""" Creates a recipe markdown file """
import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict

import jinja2


def ingredient_display(value):
    """Remove annotations on ingredients"""
    return re.sub(r"[{}]", "", value)


jinja2.filters.FILTERS["ingredient_display"] = ingredient_display


def get_output_path(input_path, output_format):
    """Re-compose the url for the output"""
    dir_name = {"md": "markdown", "html": "html"}
    output_dir = re.sub(r"^json", dir_name[output_format], os.path.dirname(input_path))
    output_name = re.sub(r"json$", output_format, os.path.basename(input_path))
    return os.path.join(output_dir, output_name)


def get_file_index(file_list, output_format):
    """Get a list of available files in a usable form"""
    index = defaultdict(lambda: {})
    for item in file_list:
        subdir = os.path.dirname(item).split("/")[-1]
        with open(item, "r", encoding="utf-8") as recipe_file:
            json_data = json.load(recipe_file)
            title = json_data["title"]
        file_link = os.path.join("../../", get_output_path(item, output_format))
        index[subdir][file_link] = title
    return index


def write_file(file_index, input_path, output_path, output_format):
    """Load a recipe json file and write it to the corresponding output dir"""
    # Load the json file
    with open(input_path, "r", encoding="utf-8") as json_file:
        recipe_data = json.load(json_file)

    # Compile the Jinja template
    with open(f"template.{output_format}", "r", encoding="utf-8") as json_file:
        template = jinja2.Template(json_file.read())

    # Write the output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(template.render(recipe=recipe_data, index=file_index))


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
    for version in formats:
        all_files_index = get_file_index(files, version)
        for file in files:
            sys.stdout.write(".")
            output_filename = get_output_path(file, version)
            write_file(all_files_index, file, output_filename, version)
    sys.stdout.write("\n")
