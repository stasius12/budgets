FROM python:3.9.7

WORKDIR /app

RUN pip3 install --upgrade pip \
    && pip3 install pipenv==2021.5.29

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN pipenv install --system --dev --deploy

COPY . /app

EXPOSE 8000
