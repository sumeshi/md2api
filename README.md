# md2api

sumeshi.github.io api converter

## Development

```console
$ uv sync --locked
$ uv run md2api . https://sumeshi.github.io posts
```

## Usage

```console
$ md2api . https://sumeshi.github.io posts
```

## Publishing

Configure a PyPI trusted publisher for the `sumeshi/md2api` repository, the
`publish.yml` workflow, and the `pypi` environment. Then push a tag that
matches the version in `pyproject.toml`:

```console
$ git tag v0.6.1
$ git push origin v0.6.1
```
