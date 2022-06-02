import os

from dotenv import load_dotenv

if os.getenv("ENV") == "local":
    load_dotenv()
