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

    # Replace the old badge or add a new one
    if "![coverage]" in content:
        content = content.replace(
            content.split("![coverage](")[1].split(")")[0],
            badge_url
        )
    else:
        content = badge_markdown + "\n\n" + content

    with open(readme_file, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    coverage = parse_coverage('coverage.xml')
    update_readme('README.md', coverage)
