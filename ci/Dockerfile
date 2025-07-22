# Use official Python 3.12 base image
FROM python:3.12-slim


WORKDIR /app

# Create a location where the test calibration files will go
RUN mkdir -p /root/Documents/cepton

COPY . .
RUN pip install --upgrade pip && pip install .

CMD ["/bin/bash"]
