import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api.improve import router as improve_router

load_dotenv()

app = FastAPI(title="Pitulung Backend")

# CORS middleware - only allow pitulung.com
allowed_origins = [
    "https://pitulung.com",
    "https://www.pitulung.com",
]

# Add localhost for development if needed
if os.getenv("ENVIRONMENT") == "development":
    allowed_origins.extend([
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ])

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Pitulung-Backend!"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


# Include routers
app.include_router(improve_router)