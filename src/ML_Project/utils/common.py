import os 
from box.exceptions import BoxValueError
import yaml
from src.ml_project.logger import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any


@ensure_annotations
def read_yaml(yaml_file_path: Path) -> ConfigBox:
    """ reads yaml file and return content from it.

    Args: 
        yaml_file_path (Path): file path 
    
    Returns:
        ConfigBox: ConfigBox object 
    
    Raises:
        ValueError: if yaml_file_path is empty 
        e: empty file
    """
    try: 
        with open(yaml_file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError: 
        raise ValueError("yaml file is empty..!")
    except Exception as e:
        raise e

@ensure_annotations  
def create_directories(directory_paths: list, verbose=True):
    """
    creates list of directories.
    
    Args: 
     directory_paths (list): list of directories paths.
     verbose (bool): if true, then it will ignores logging.  
    """ 
    for directory_path in directory_paths:
        os.makedirs(directory_path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {directory_path}")