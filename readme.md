# Introduction

This web application has been developed on Ubuntu distributions and has been deployed on the Google Cloud Platform.

# Pre-Requisites

  ```sudo apt-get update
     sudo apt-get install -y python3
     sudo apt-get install -y python3-pip
     sudo apt-get install virtualenv
     sudo apt-get git
```
# Run The Application

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

# Deploying on SystemD
  To deploy the app;ication use the following:
    ```
    sudo apt-get update
    sudo apt-get -y install python3-pip
    sudo apt-get -y install virtualenv
    sudo apt-get -y install git
    # install the service script
    sudo cp flask-app.service /etc/systemd/system/
    # reload the service scripts
    sudo systemctl daemon-reload
    # stop the old service
    sudo systemctl stop flask-app
    # install the application files
    install_dir=/opt/flask-app
    sudo rm -rf ${install_dir}
    sudo mkdir ${install_dir}
    sudo cp -r ./* ${install_dir}
    sudo chown -R pythonadm:pythonadm ${install_dir}
    # configure python virtual environment and install dependencies
    sudo su - pythonadm << EOF
    cd ${install_dir}
    virtualenv -p python3 venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    EOF
    ```
# Deploying on Docker

  To deploy the application on Docker use the following:
  ```
    git clone https://www.github.com/alexnderkong/individual.git
    cd individual
    Docker Build . -t flask
    Docker Run -d -p 5000:5000 flask
  ```
  
