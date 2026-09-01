import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Carrega as variáveis de ambiente (útil apenas para o seu ambiente local)
if os.path.exists(".env"):
    load_dotenv()

# 2. Fazemos a inicialização na própria leitura do arquivo (resolve a ordem)
if not firebase_admin._apps:
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    
    # Se estamos localmente E o arquivo JSON realmente existe na pasta
    if cred_path and os.path.exists(cred_path):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    else:
        # Se estamos no Cloud Run (o JSON não existe lá, então ele usa as permissões do próprio Google Cloud)
        firebase_admin.initialize_app()

# 3. AGORA SIM, com o Firebase inicializado, criamos a conexão com o banco
db = firestore.client()

def init_firebase():
    # Mantemos a função vazia apenas para não quebrar o seu main.py, 
    # já que a inicialização real já foi feita acima de forma segura.
    pass