# Data engineer challenges with Bigquery operations

This project will involve creating a table in BigQuery and loading data into it via Python. 

## Technologies to use

* BigQuery (Free trial GCP account)
* Python

## Problem statement

In "data" directory, 3 json files are provided:

1. customers_1.json
2. customers_2.json
3. customers_3.json

Each file contains a few records of customer data (in newline delimited json format). Start by creating a project in BigQuery - you'll be able to complete this exercise using a free trial GCP account. Then create a Python script that accomplishes the following three tasks:

1. Use customers_1.json to create a table in Python and load the data into it.
2. Load customers_2.json into the table using a load job.
    * Note: The file customers_2.json has additional fields, and you'll need to update the schema of your table. Try to do this without manually specifying the names of the new fields.
3. Load the file customers_3.json into the table using a streaming insert.
    * Note: As before, the file customers_3.json includes another schema change.

## Use the following instructions to achive the solutions

    * You need to have python & Jupyter lab or suitable python editor installed in your system.

## Supported Python Versions for the Google BigQuery Python Client
* Python >= 3.6, < 3.10

## Unsupported Python Versions for the Google BigQuery Python Client
* Python == 2.7, Python == 3.5.

## Make sure to have supported python version(s) installed 
* If you want to attach differnt/supported Python version for your project
***
    Example : -
    py -m virtualenv -p="D:\Python\Python39\python.exe" venv
*** 

## To install Jupyterlab please follow bellow link
<a href="https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html" target="_blank">Jupyterlab</a>
***
    pip install jupyterlab
***

## Start JupyterLab using:
***
    jupyter lab
***

## Installed Python Version for this project
* Python == Python 3.9.6

* Make sure to run command promt(cmd) as an Adminstrator.
* And traverse to the project location and Install & activate your virtual environment before installing any pyhton packeges.

### Install virtualenv module for your system
***
    pip install virtualenv
***

### Create virtual env for your project location
***
    D:\Python_Projects\data-engineer-challenge-test>py -m virtualenv venv
***

### Activate virtual environment
***
    D:\Python_Projects\data-engineer-challenge-test>.\venv\scripts\activate
***

### Make sure to update pip package in your virtual env
***
    D:\Python_Projects\data-engineer-challenge-test>py -m pip install --upgarde pip
***

### For the deactivating virtual env
***
    (venv) D:\Python_Projects\data-engineer-challenge-test>deactivate
***

### Install Python Client for Google BigQuery
<a href="https://googleapis.dev/python/bigquery/latest/index.html" target="_blank">Python Client for Google BigQuery</a>
***
    pip install google-cloud-bigquery
***

### Install pipreqs module for project requirments.txt file generation
<a href="https://pypi.org/project/pipreqs/" target="_blank">Link for pipreqs</a>
***
    pip install pipreqs
***

### Install python-dotenv module for project's environment variable read 
<a href="https://pypi.org/project/python-dotenv/" target="_blank">Link for python-dotenv</a>
***
    pip install python-dotenv
***

## How to read enviroment variable GOOGLE_APPLICATION_CREDENTIALS from .env file

* place your Google Cloud Service Account key file under the project folder "\keys"
* make .env file under your project directory root
* open .env file with your text editor & put following line on it 
***
    GOOGLE_APPLICATION_CREDENTIALS=".\keys\key.json"
***

### Launch "jupyter lab" in a seperate terminal/command prompt
***
    (venv) D:\Python_Projects\data-engineer-challenge-test>jupyter lab
***

# Small diagnosis tips
### If your Installed all your requirement but have problems like bellow
***
    ModuleNotFoundError: No module named 'google.cloud'
***

### Try followings at your jupyter lab cell
***
    import sys
    !{sys.executable} -m pip show google-cloud-bigquery
***

### If above code block showing any errors, do following
***
    !{sys.executable} -m pip install --upgrade google-cloud-bigquery
***

### Now trigger the same command again
***
    !{sys.executable} -m pip show google-cloud-bigquery
***

### Do follow same steps for the other packages too.
