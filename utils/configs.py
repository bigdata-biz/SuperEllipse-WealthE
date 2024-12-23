import os
BASE_DIR = os.getenv("HOME")
DATA_DIR = os.path.join(BASE_DIR, "assets", "data")
INDEX_DIR = os.path.join(DATA_DIR,"index")
DB_DIR = os.path.join(DATA_DIR, "chroma_db")
RAW_DATA_DIR=os.path.join(DATA_DIR, "raw")
DATASET_URL="https://zerodha.com/varsity/chapter-sitemap2.xml"
DATASET_PATH=os.path.join(RAW_DATA_DIR, "chapters.txt")
EVAL_DATA_DIR = os.path.join(DATA_DIR, "questions")
IMAGE_DIR = os.path.join(DATA_DIR, "images")
VECTORDB_COLLECTION ="quickstart-ollama"
OLLAMA_BASE_URL=os.getenv("OLLAMA_BASE_URL", "127.0.0.1:8080")
UTILS_DIR = os.path.join(BASE_DIR, "utils")
DEFAULT_LLM ="llama3"
DEFAULT_EMBEDDING_MODEL="BAAI/bge-small-en-v1.5"
DEFAULT_CHAT_MODE = "condense_plus_context"
LOG_PATH = os.path.join(BASE_DIR, "utils","logs")
TRULENS_DB_PATH= os.path.join(DATA_DIR, "trulens_db")
TRULENS_DB_URL=f"sqlite:///{TRULENS_DB_PATH}/default.sqlite"
LLM_EXPERIMENT_NAME= "LLM Evaluations for WealthE"
