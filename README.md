#
# Customer Support Chatbot with Rasa
This repository hosts the code and resources for a customer support chatbot built with Rasa. The bot was developed as a solution to streamline and automate customer support services, using real-world customer interactions data from Zendesk transcripts.

# Project Overview
The project started with the extraction and analysis of customer interaction data from Zendesk. Through various Natural Language Processing techniques, including Topic Modeling and t-SNE clustering, key themes and common customer queries were identified. These insights guided the design and development of the Rasa chatbot.

The bot was designed to handle the most frequent customer queries, thereby reducing the workload on human customer service agents and increasing the efficiency of the support service.

The chatbot was subsequently dockerized for consistent deployment and hosted on the cloud platform Okteto, demonstrating its scalability and adaptability to different infrastructures.

## Rasa_Chatbot on Cloud
End to end rasa chatbot that has been trained and deployed to the cloud.
The endpoint is: https://dockersrc-sanchitsharma10.cloud.okteto.net/webhooks/rest/webhook you can use a application/service like Postman to post JSON requests to it such as:
{
    "sender": "user",
    "message": "Hello"
}

For Headers just add "Content-Type" and its Value is "application/json" 

# Key Features
Data Extraction and Analysis: Used Python scripts to extract customer lines from Zendesk transcripts. Analyzed the data using techniques like Topic Modeling and t-SNE clustering to uncover common issues and queries.
Chatbot Development with Rasa: Built a Rasa chatbot capable of handling the most common customer queries. The bot was designed to provide quick, automated responses to customer queries.
Dockerization: Containerized the chatbot application using Docker, facilitating easy deployment and scaling.
Cloud Deployment: Deployed the dockerized chatbot on Okteto, demonstrating its adaptability and scalability in a cloud environment.

# How to Run
## Docker Container
This application is containerized using Docker, which means you can easily run it locally if you have Docker installed. If you don't already have Docker, you can download and install it from [here](https://www.docker.com/products/docker-desktop).

Follow these steps to get the application running:

### Steps
1. Navigate to the project directory.

  ```bash  
  cd yourrepository
  ```

2. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/SanchitSharma10/Rasa_Chatbot.git
   ```
   
3. Build the Docker image. Replace image_name with the name you want to give to the Docker image.

   ```bash
   docker build -t image_name .
   ```
   
4. Run the Docker container. Replace image_name with the name of the Docker image you just built.

   ```bash
   docker run -p 5000:5000 image_name
   ```
   
This will start the application on your local machine. You can then access it by navigating to http://localhost:5000 in your web browser.

Please note, you may need to adjust the port number (5000 in this example) based on your application configuration.


*This is a general guide, and you may need to adjust these instructions based on the specifics of your project and Docker setup.

## Manual Setup for M1 Mac

This guide will help you set up and run the project manually on an M1 Mac. We'll be using Conda for package and environment management.


1. Navigate to the project directory.

    ```bash
    cd yourrepository
    ```

2. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/SanchitSharma10/Rasa_Chatbot.git
   ```
  
3. Create a new Conda environment. Replace env_name with the name you want to give to your new environment.

    ```bash
    conda create --name env_name python=3.8
    ```

4. Activate the newly created environment.

    ```bash
    conda activate env_name
    ```

5. Install Rasa 3.0 or higher in the active Conda environment.

    ```bash
    pip install rasa
    ```

6. Ensure the Rasa version is 3.0 or higher by running:

   ```bash
   rasa --version
   ```
   
7. Install the project's dependencies. If you have a requirements.txt file in the project, you can use the following command:

   ```bash
   pip install -r requirements.txt
   ```

Start the Rasa server.
   
   ```bash
   rasa run
   ```

You can now interact with the bot by navigating to http://localhost:5005 in your web browser.

Please note, you may need to adjust these instructions based on the specifics of your project setup.

*This guide assumes the user is somewhat familiar with command line interface.


### Prerequisites

Ensure you have the following installed on your system:

- Conda: If you don't have it installed, download it from [here](https://docs.conda.io/en/latest/miniconda.html#macosx-installers).
- Git: You can check if Git is installed by opening a terminal and typing `git --version`. If it's not installed, you can download it from [here](https://git-scm.com/downloads).

   
# Future Improvements

  ## Additional features to add to the chatbot:

  1. GPT-2 processing of large text responses.
  2. Adding Api calls to a database.
  3. Adding additional languages.
  4. Improving the accuracy above benchmark standards.
  5. integration with additional cloud services (VM's)

# Acknowledgements
This project was undertaken as an initiative to enhance the efficiency of customer support services at (ACTO).




