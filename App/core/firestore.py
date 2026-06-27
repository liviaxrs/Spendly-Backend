import os
from dotenv import load_dotenv
from google.cloud import firestore

# Carrega o .env apenas se o arquivo existir (ambiente local)
if os.path.exists(".env"):
    load_dotenv()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

db = firestore.Client()