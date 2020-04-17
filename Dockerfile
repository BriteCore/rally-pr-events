FROM python:3.7-alpine

LABEL "com.github.actions.name"="Update Rally Items"
LABEL "com.github.actions.description"="Update Rally stories based on PR events."

COPY *.py /

COPY requirements.txt /requirements.txt

RUN apk update \
    && apk upgrade \
    && apk add --no-cache git openssh
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "/entrypoint.py"]
