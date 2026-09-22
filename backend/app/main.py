from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Grihome API",
    description="Household Document & Warranty Expiry Tracker",
    version="0.1.0",
)

# Allow the Vite dev server (frontend) to call this API during development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Grihome API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}