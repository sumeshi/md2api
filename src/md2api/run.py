# coding: utf-8
import sys
from pathlib import Path
from typing import List
from datetime import datetime

from git import Repo
from markdown import Markdown


def parse_markdown_filepaths(path: str) -> List[Path]:
    root = Path(path)
    return root.glob('**/*.md') if root.is_dir() else [root]


def convert_markdown_to_html(text: str) -> str:
    md = Markdown()
    return md.convert(text)


def get_lastcommit_date(path: str) -> datetime:
    repo = Repo('.')
    latest_commit = repo.iter_commits('--all', max_count=1, paths=path).__next__()
    latest_committed_date = latest_commit.committed_date
    return datetime.fromtimestamp(latest_committed_date)

def main():
    target_path = Path(sys.argv[1])
    markdown_files = parse_markdown_filepaths(target_path)

    for f in markdown_files:
        print(f)
        print(convert_markdown_to_html(f.read_text()))
        print(get_lastcommit_date(f))
        print()

if __name__ == '__main__':
    main()