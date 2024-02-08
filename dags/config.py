from loguru import logger
from pathlib import Path
from dotenv import load_dotenv

# Setting up the paths
DAGS_DIR = Path(__file__).parent
PROJECT_DIR = DAGS_DIR.parent

# Setting up the project directories
LOGS_DIR = PROJECT_DIR / "logs"
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / ".output"
PYENV_DIR = PROJECT_DIR / "env"

# Setting up the environment
ENV_FILE = PYENV_DIR / ".env"
if not ENV_FILE.exists():
    raise FileNotFoundError(f"Python environment file not found: \n{ENV_FILE}")

load_dotenv(ENV_FILE)