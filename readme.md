#Introduction

This web application has been developed on Ubuntu distributions and has been deployed on the Google Cloud Platform.

#Pre-Requisites

  ```sudo apt-get update
     sudo apt-get install -y python3
     sudo apt-get install -y python3-pip
     sudo apt-get install virtualenv
     sudo apt-get git
```
#Run The Application

  Get the Git Repository using:
    ```
      git clone https://www.github.com/alexnderkong/individual.git
      cd individual/application
      pip3 install -r requirements.txt
    ```
  Activate the virtual Environment:
     ``` 
      virtualenv -p python3 venv
      source venv/bin/activate
      . venv/bin/activate
     ``` 
  Run the Application Locally:
    ```
    python3 run.py
    ```
  Follow the GCP external IP address.
  append :5000/ to the address.
  Allow unsecure access to the website.


#Deploying on Docker

  To deploy the application on Docker use the following:
  ```
    git clone https://www.github.com/alexnderkong/individual.git
    cd individual
    Docker Build . -t flask
    Docker Run -d -p 5000:5000 flask
  ```
  
