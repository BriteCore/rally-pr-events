FROM 3.8.2-alpine3.11

COPY entrypoint.py /entrypoint.py
COPY requirements.txt /requirements.txt

RUN echo "$values"

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
