FROM python:3.7-slim

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY main.py /app/

WORKDIR /app
VOLUME /output
ENTRYPOINT ["/app/main.py"]
