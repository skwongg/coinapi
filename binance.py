import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_KEY=os.environ.get("BINAN_API_KEY")
SECRET_KEY=os.environ.get("BINAN_SECRET_KEY")
