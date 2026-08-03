from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.document_api import router as document_router
from app.api.auth_api import router as auth_router
from ai.router import router as ai_router
from app.api.user_api import router as user_router

app= FastAPI(
    title="LUMINA AI",
    version= "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)
app.include_router(auth_router)
app.include_router(document_router)
app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI"
    }