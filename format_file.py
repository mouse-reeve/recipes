""" Creates a recipe markdown file """
import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

import filters

FILES_PATH = "json/**/*.json"
ENV = Environment()
ENV.loader = FileSystemLoader("templates/")
ENV.filters["ingredient_display"] = filters.ingredient_display
ENV.filters["ingredient_data"] = filters.ingredient_data


def get_output_path(input_path, output_format):
    """Re-compose the url for the output"""
    dir_name = {"md": "markdown", "html": "html"}
    output_dir = re.sub(r"^json", dir_name[output_format], os.path.dirname(input_path))
    output_name = re.sub(r"json$", output_format, os.path.basename(input_path))
    return os.path.join(output_dir, output_name)


def get_file_index(output_format):
    """Get a list of available files in a usable form"""
    file_list = glob.glob(FILES_PATH)
    index = defaultdict(lambda: {})
    for item in file_list:
        subdir = os.path.dirname(item).split("/")[-1]
        with open(item, "r", encoding="utf-8") as recipe_file:
            json_data = json.load(recipe_file)
            title = json_data["title"]
        link_path = "/".join(item.split("/")[1:])
        file_link = re.sub(r"json$", output_format, link_path)
        index[subdir][file_link] = title
    return index


def write_file(file_index, input_path, output_path, output_format):
    """Load a recipe json file and write it to the corresponding output dir"""
    # Load the json file
    with open(input_path, "r", encoding="utf-8") as json_file:
        recipe_data = json.load(json_file)

    # Compile the Jinja template
    template = ENV.get_template(f"{output_format}/recipe.{output_format}")
    subdir = os.path.dirname(output_path).split("/")[-1]

    # Write the output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(
            template.render(recipe=recipe_data, current_dir=subdir, index=file_index)
        )


def write_index_file(file_index, output_format):
    """Create the file index"""
    output_path = get_output_path("json/index.json", output_format)
    # Compile the Jinja template
    template = ENV.get_template(f"{output_format}/index.{output_format}")
    subdir = os.path.dirname(output_path).split("/")[-1]

    # Write the output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(template.render(current_dir=subdir, index=file_index))


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

    files = glob.glob(FILES_PATH) if compile_all else [filename]
    formats = [format_preference] if format_preference else format_choices

    # either get all the files or one specific file
    sys.stdout.write(f"Writing {len(files)} file(s):\n")
    for version in formats:
        all_files_index = get_file_index(version)

        write_index_file(all_files_index, version)

        for file in files:
            sys.stdout.write(".")
            output_filename = get_output_path(file, version)
            write_file(all_files_index, file, output_filename, version)
    sys.stdout.write("\n")
