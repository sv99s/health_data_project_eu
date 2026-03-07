
from pathlib import Path

# ==============================
# Project Root Path
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# Data Paths
# ==============================
RAW_DATA_PATH = BASE_DIR / "data" / "raw"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed"
CURATED_DATA_PATH = BASE_DIR / "data" / "curated"

# ==============================
# SQL Folder Path
# ==============================
SQL_PATH = BASE_DIR / "sql"

# ==============================
# Ensure directories exist
# ==============================
for path in [PROCESSED_DATA_PATH, CURATED_DATA_PATH]:
    path.mkdir(parents=True, exist_ok=True)