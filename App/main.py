from fastapi import FastAPI
from App.routes import user_route, category_route
from App.routes import summary_route, transaction_route

app = FastAPI()

app.include_router(user_route.router)
app.include_router(category_route.router)
app.include_router(transaction_route.router)
app.include_router(summary_route.router)