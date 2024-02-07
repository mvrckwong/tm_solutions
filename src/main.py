from os import getenv, environ
from dotenv import load_dotenv
from pathlib import Path
from loguru import logger

from google.cloud import bigquery

# General Directories
SRC_DIR = Path(__file__).parent
PROJECT_DIR = SRC_DIR.parent

LOGS_DIR = PROJECT_DIR / "logs"
DATA_DIR = PROJECT_DIR / "data"

# Environment 
ENV_FILE = SRC_DIR / ".env"
BQUERY_JSON_FILE = SRC_DIR / "golden-ego-396703-9dbf90079b0f.json"

# Load Environment
load_dotenv(ENV_FILE)
environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(BQUERY_JSON_FILE)

# Sample Query
client = bigquery.Client()

sql_query = """
SELECT *
FROM `bigquery-public-data.san_francisco.bikeshare_stations`
LIMIT 50
"""

query_job = client.query(sql_query)
query_results = query_job.result()

logger.warning("Sample")