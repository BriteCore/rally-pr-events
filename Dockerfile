FROM python:latest

COPY entrypoint.py /entrypoint.py
COPU requirements.txt /requirements.txt

RUN echo "$values"

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
