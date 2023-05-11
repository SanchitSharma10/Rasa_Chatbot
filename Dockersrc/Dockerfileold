FROM rasa/rasa:3.0.4-full

USER root

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim
# Copy your Rasa project files
COPY . /app

# Set the working directory
WORKDIR /app

# Install any additional dependencies specified in your requirements.txt
# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip

RUN pip install -r requirements.txt

# Expose the Rasa port
EXPOSE 5005
