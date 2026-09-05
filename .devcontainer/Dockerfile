FROM python:3.11-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.10.4 /uv /uvx /bin/

RUN apt -y update && apt upgrade -qqy && apt -y install \
    curl \
    gcc \
    git \
    fish

RUN chsh -s /usr/bin/fish
