from fastapi import FastAPI
from src.router import router as crypto_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.include_router(crypto_router)

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


