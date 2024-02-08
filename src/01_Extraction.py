from os import getenv, environ
from dotenv import load_dotenv
from pathlib import Path
from loguru import logger
import pandas as pd 

from google.cloud import bigquery
from typing import List
from dataset import ecommerce_dataset

# General Directories
SRC_DIR = Path(__file__).parent
PROJECT_DIR = SRC_DIR.parent

LOGS_DIR = PROJECT_DIR / "logs"
DATA_DIR = PROJECT_DIR / "data"

# Load the Environment
ENV_FILE = SRC_DIR / ".env"
load_dotenv(ENV_FILE)

# Load and Set BigQuery Credentials
BIGQUERY_JSON_FILE = SRC_DIR / getenv("BIGQUERY_JSON_FILE")
environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(BIGQUERY_JSON_FILE)

def query_to_df(bigquery_dataset:str) -> pd.DataFrame.to_csv:
    """ Query the data from bigquery and save it to pandas dataframe."""
    client = bigquery.Client()
    sql_query = f"""
        SELECT * FROM `{bigquery_dataset}`
    """
    return client.query(sql_query).to_dataframe()

@logger.catch
def main(link_datasets:List[str], test=False):
    # Loop through the Bigquery Dataset selected
    for index, dataset in enumerate(link_datasets):
        name_list = dataset.split(".")[-2:]
        name = "-".join(name_list) + ".csv"
        
        # Query and Save the data
        df = query_to_df(dataset)
        df.to_csv(DATA_DIR / name)
        
        if index==0 and test==True: 
            break
        
    return True

if __name__ == "__main__":
    # Setting the current dataset
    current_dataset = ecommerce_dataset
    debug_stage = False
    
    # Run the main function
    if main(current_dataset, test=debug_stage):
        logger.info("Main function successfully executed.")