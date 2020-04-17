FROM python:3.8.2-slim

COPY entrypoint.py /entrypoint.py
COPY requirements.txt /requirements.txt

RUN echo "$values"

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
