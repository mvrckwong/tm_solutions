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
    sql_query = f"SELECT * FROM `{bigquery_dataset}`"
    return client.query(sql_query).to_dataframe()
@logger.catch
def main(dataset:List[str]):
    # Loop through the Bigquery Dataset selected
    # sample = "bigquery-public-data.thelook_ecommerce.distribution_centers"
    # df = query_to_df(sample)
    # df.to_csv(DATA_DIR / "sample.csv")
    
    
    
    
    return True

if __name__ == "__main__":
    # Setting the current dataset
    current_dataset = ecommerce_dataset
    
    # Run the main function
    if main(current_dataset):
        logger.info("Main function successfully executed.")