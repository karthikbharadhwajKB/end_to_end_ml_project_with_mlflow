import os 
from pathlib import Path
import logging

# logging 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "ml_project"

# list of files we need to create
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
    "test.py"
]


for filepath in list_of_files:
    # convert filepath to os dependent path (Windows path)
    filepath = Path(filepath)
    # seperating file folders & files
    filedir, filename = os.path.split(filepath) 

    # if filedir is not empty then we will create a directory
    if filedir != "":
        # creating directory (it will create all intermediate folders also)
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # checking if filepath already exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # if filepath not exists
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else: 
        # if filepath already exists
        logging.info(f"{filepath} already exists...!")
