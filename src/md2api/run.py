# coding: utf-8
import sys
from pathlib import Path
from typing import List

from markdown import Markdown


def parse_markdown_filepaths(path: str) -> List[Path]:
    root = Path(path)
    return root.glob('**/*.md') if root.is_dir() else [root]

def convert_markdown_to_html(text: str) -> str:
    md = Markdown()
    return md.convert(text)


def main():
    target_path = Path(sys.argv[1])
    markdown_files = parse_markdown_filepaths(target_path)

    for f in markdown_files:
        print(f)
        print(convert_markdown_to_html(f.read_text()))

if __name__ == '__main__':
    main()