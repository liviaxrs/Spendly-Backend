from fastapi import FastAPI
from App.routes import user_route, category_route
from App.routes import summary_route, transaction_route
from fastapi.middleware.cors import CORSMiddleware
from App.core.firestore import init_firebase

init_firebase()
app = FastAPI()

origins = [
    "http://localhost:5173"
    ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(user_route.router)
app.include_router(category_route.router)
app.include_router(transaction_route.router)
app.include_router(summary_route.router)