FROM python:latest

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip3 install -U pip
RUN pip3 install -r /tmp/requirements.txt

# copy over our src code
COPY src /app
WORKDIR /app

EXPOSE 8000
CMD ["python3", "main.py"]