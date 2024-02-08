from os import getenv, environ
from dotenv import load_dotenv
from pathlib import Path
from loguru import logger
from pyspark.sql import SparkSession
from google.cloud import bigquery
import shutil
from typing import List
from dataset import ecommerce_dataset  # Assuming this module exists and is correctly imported

# General Directories
SRC_DIR = Path(__file__).parent.absolute()
PROJECT_DIR = SRC_DIR.parent

LOGS_DIR = PROJECT_DIR / "logs"
DATA_DIR = PROJECT_DIR / "data"

# Load the Environment
ENV_FILE = SRC_DIR / ".env"
load_dotenv(ENV_FILE)

# Load and Set BigQuery Credentials
BIGQUERY_JSON_FILE = SRC_DIR / getenv("BIGQUERY_JSON_FILE")
environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(BIGQUERY_JSON_FILE)

def query_to_df(spark: SparkSession, bigquery_dataset: str):
    """Query the data from BigQuery and save it to a Spark DataFrame."""
    return spark.read.format("bigquery").option("table", bigquery_dataset).load()

def save_single_csv(df, name):
    """Save DataFrame as a single CSV with a specific name."""
    temp_dir = DATA_DIR / "temp"
    df.coalesce(1).write.mode("overwrite").option("header", "true").csv(str(temp_dir))
    
    # Find the part-file and move it to the desired path
    part_file = next(temp_dir.glob("part-*.csv"))
    desired_path = DATA_DIR / f"{name}.csv"
    
    shutil.move(str(part_file), str(desired_path))
    
    # Clean up: remove temporary directory
    shutil.rmtree(str(temp_dir))

@logger.catch
def main(link_datasets: List[str], test=False):
    # Create Spark Session
    spark = SparkSession.builder \
        .appName("BigQuery to Spark Example") \
        .config('spark.jars.packages', 'com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.21.0') \
        .getOrCreate()

    # Loop through the BigQuery Dataset selected
    for index, dataset in enumerate(link_datasets):
        logger.debug(f"Current dataset: {dataset}")
        name_list = dataset.split(".")[-2:]
        name = "-".join(name_list)
        
        # Query and Save the data
        df = query_to_df(spark, dataset)
        
        # Save DataFrame as a single CSV file with a specific name
        save_single_csv(df, name)
        
        if index == 0 and test == True:
            break
        
    spark.stop()
    return True

if __name__ == "__main__":
    # Setting the current dataset
    current_dataset = ecommerce_dataset
    debug_stage = False
    
    # Run the main function
    if main(current_dataset, test=debug_stage):
        logger.info("Main function successfully executed.")