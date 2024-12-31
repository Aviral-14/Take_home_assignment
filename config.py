# config.py
##OPENAI_API_KEY = "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"
#DATA_PATH = "D:\Assignment\data"
#EMBEDDINGS_PATH = "D:\Assignment\embeddings"
#OUTPUTS_PATH = "D:\Assignment\output"
#MODEL_NAME = "text-embedding-ada-002"  # OpenAI embedding model

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Path Configuration
BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data"
OUTPUTS_PATH = BASE_DIR / "outputs"
LOGS_PATH = BASE_DIR / "logs"

# Create directories if they don't exist
for path in [DATA_PATH, OUTPUTS_PATH, LOGS_PATH]:
    path.mkdir(parents=True, exist_ok=True)

# Model Configuration
CHAT_MODEL = "gpt-4"
EMBEDDING_MODEL = "text-embedding-ada-002"

# Processing Configuration
BATCH_SIZE = 15
MAX_TOKENS = 1000
TEMPERATURE = 0.7

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")