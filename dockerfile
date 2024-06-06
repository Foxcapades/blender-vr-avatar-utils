FROM python:3.11.9-alpine3.20

RUN pip install --no-cache-dir python-minifier
WORKDIR /tmp/workspace

CMD python --version
