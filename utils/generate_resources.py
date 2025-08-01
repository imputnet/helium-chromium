# Copyright 2025 The Helium Authors
# You can use, redistribute, and/or modify this source code under
# the terms of the GPL-3.0 license that can be found in the LICENSE file.
"""
Generates scaled resources for Helium branding
"""

import os
import sys
from PIL import Image


def scale_image(input_file, size, output_path):
    """
    Scales the square image to provided size and saves it
    """
    img = Image.open(input_file)
    img.thumbnail((size, size))

    # make sure output path exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    img.save(output_path, optimize=True)


def generate_resources(resource_list, resource_dir):
    """
    Parses the resource list and generates resources
    for each valid line
    """
    with open(resource_list, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            line_parts = line.split()

            if len(line_parts) != 3:
                raise ValueError(f"Line {line_number} in the resource file is invalid.")

            input_file = os.path.join(resource_dir, line_parts[0])
            size = int(line_parts[1])
            output_file = os.path.join(resource_dir, line_parts[2])

            scale_image(input_file, size, output_file)
            print(f"Created {line_parts[2]}")


def main():
    """CLI entrypoint"""
    if len(sys.argv) != 3:
        print(
            "Usage: python3 generate_resources.py " \
            "<generate_resources.txt> <resources_dir>"
        )
        sys.exit(1)

    resource_list = sys.argv[1]
    resource_dir = sys.argv[2]

    generate_resources(resource_list, resource_dir)


if __name__ == "__main__":
    main()
