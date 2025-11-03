from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api.improve import router as improve_router

load_dotenv()

app = FastAPI(title="Pitulung Backend")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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