FROM python:3.7-alpine

LABEL "com.github.actions.name"="Update Rally Items"
LABEL "com.github.actions.description"="Update Rally stories based on PR events."

COPY *.py /

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Setup docker entry point
COPY entrypoint.sh /usr/local/bin/

RUN chmod 777 /usr/local/bin/entrypoint.sh \
    && ln -s /usr/local/bin/entrypoint.sh /

ENTRYPOINT ["entrypoint.sh"]
