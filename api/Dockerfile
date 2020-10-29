FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /minventory
WORKDIR /minventory
ADD requirements.txt /minventory/
RUN pip install -r requirements.txt
ADD . /minventory/
