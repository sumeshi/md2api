# coding: utf-8
import sys
from pathlib import Path
from typing import List, NamedTuple, Optional
from datetime import datetime

from git import Repo
from markdown import Markdown


class Document(NamedTuple):
    title: str
    path: str
    html_text: str
    published_at: datetime


def parse_markdown_filepaths(path: str) -> List[Path]:
    root = Path(path)
    return root.glob('**/*.md') if root.is_dir() else [root]


def convert_markdown_to_html(text: str) -> str:
    md = Markdown()
    return md.convert(text)


def get_lastcommit_date(path: str) -> Optional[datetime]:
    repo = Repo('.')

    try:
        latest_commit = repo.iter_commits('--all', max_count=1, paths=path).__next__()
        latest_committed_date = latest_commit.committed_date
        return datetime.fromtimestamp(latest_committed_date)
    except StopIteration:
        return None


def main():
    target_path = Path(sys.argv[1])
    markdown_files = parse_markdown_filepaths(target_path)

    output_path = Path('docs')

    documents = [
        Document(
            title = markdown.name,
            path = str(markdown),
            html_text = convert_markdown_to_html(markdown.read_text()),
            published_at = get_lastcommit_date(markdown)
        ) for markdown in markdown_files if get_lastcommit_date(markdown)
    ]

    for f in documents:
        print(f)


if __name__ == '__main__':
    main()