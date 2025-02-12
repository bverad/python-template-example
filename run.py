from fastapi import FastAPI
from app.views.document_view import router

app = FastAPI(
    title="Document Processing API",
    description="API for processing various document types and extracting text content",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1") 