import mlflow
import os
import logging
from src.utils.common import read_yaml,create_directories,get_unique_log_path

STAGE = "MAIN"  #Stage name for logs 
# Config parameters
config_path = "configs/config.yaml"
config = read_yaml(config_path)
LOG_DIR = config["LOG_DIR"]

#Logger configuration 
create_directories([LOG_DIR])
LOG_FILENAME = get_unique_log_path(LOG_DIR)
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s] : %(message)s",
    filemode="a"
)

def main():
 
    with mlflow.start_run() as run:
        # mlflow.run(".","get_data",parameters={},use_conda="false") # alternate way to pass parameters
        mlflow.run(".","get_data",use_conda="false")
        mlflow.run(".","training",use_conda="false")
    

if(__name__ == "__main__"):
    try:
        logging.info("\n*********MLFlow CNN classifier**********")
        logging.info(f">>>> Stage {STAGE} Started <<<<")
        main()
        logging.info(f">>>> Stage {STAGE} Completed <<<<")

    except Exception as e:
        logging.exception(e)
        raise e
