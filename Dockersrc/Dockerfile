FROM python:3.7.7-stretch AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip
RUN pip install transformers

RUN pip install rasa==3.0.4
RUN pip install websockets==9.1

COPY config.yml config.yml
COPY domain.yml domain.yml
COPY credentials.yml credentials.yml
COPY endpoints.yml endpoints.yml
COPY data /app/data
COPY models /app/models

EXPOSE 5005
CMD ["--help"]
