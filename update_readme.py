import xml.etree.ElementTree as ET
import os

def parse_coverage(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    line_rate = float(root.get('line-rate'))
    coverage_percentage = round(line_rate * 100, 2)
    return coverage_percentage

def update_readme(readme_file, coverage):
    badge_url = f"https://img.shields.io/badge/coverage-{coverage}%25-brightgreen"
    badge_markdown = f"![coverage]({badge_url})"

    with open(readme_file, 'r') as file:
        content = file.read()

    # Replace the old badge (assuming it's in a specific format)
    new_content = content
    if "![coverage]" in content:
        new_content = content.replace(
            content.split("![coverage](")[1].split(")")[0],
            badge_url
        )
    else:
        # Add the badge at the top if it's not present
        new_content = badge_markdown + "\n\n" + content

    with open(readme_file, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    coverage = parse_coverage('coverage.xml')
    update_readme('README.md', coverage)
