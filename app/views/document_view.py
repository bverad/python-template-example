from fastapi import APIRouter, UploadFile, File
from ..services.document_processor import DocumentProcessor
from ..schemas.response import ProcessingResponse

router = APIRouter()
document_processor = DocumentProcessor()

@router.post("/process-document", response_model=ProcessingResponse)
async def process_document(file: UploadFile = File(...)):
    """
    Process uploaded document and extract text content.
    
    Accepts PDF, DOC, DOCX, and TXT files.
    Returns extracted text content along with processing metadata.
    """
    if file.content_type not in [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/plain'
    ]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    return await document_processor.process_document(file) 