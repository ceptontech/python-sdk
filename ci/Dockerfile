# Use official Python 3.12 base image
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install .

CMD ["/bin/bash"]
