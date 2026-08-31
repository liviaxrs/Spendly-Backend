import os
from dotenv import load_dotenv
from google.cloud import firestore
import firebase_admin


if os.path.exists(".env"):
    load_dotenv()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

db = firestore.Client()
def init_firebase():
    if not firebase_admin._apps:
        firebase_admin.initialize_app()