FROM python:3.11.0-bullseye

RUN apt -y update && apt upgrade -qqy && apt -y install \
    curl \
    gcc \
    git \
    fish

RUN chsh -s /usr/bin/fish
RUN pip install -U pip && pip install poetry