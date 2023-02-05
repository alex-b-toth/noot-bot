FROM python:3.11-slim-bullseye

ARG app_name=noot_bot
ARG base_directory=telegram_bot

WORKDIR /${base_directory}

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /${base_directory}/app

CMD ["python", [".${base_directory}/app/${app_name}.py"]]