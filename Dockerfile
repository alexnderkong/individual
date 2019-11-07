FROM ubuntu:latest
FROM python:latest
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python-pip
RUN pip install cryptography
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/python", "run.py"]
