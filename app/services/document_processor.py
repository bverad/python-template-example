from datetime import datetime
import pytesseract
from pdf2image import convert_from_bytes
from docx import Document
import PyPDF2
import io
from ..schemas.response import ProcessingResponse
from .ocr_service import OCRService
from .table_extractor import TableExtractor
import logging
from fastapi import HTTPException
from typing import List, Dict
import traceback

logger = logging.getLogger('document_processor')

class DocumentProcessingError(Exception):
    """Custom exception for document processing errors"""
    pass

class DocumentProcessor:
    def __init__(self):
        self.ocr_service = OCRService()
        self.table_extractor = TableExtractor()
        self.supported_extensions = {'txt', 'pdf', 'doc', 'docx'}

    async def process_document(self, file) -> ProcessingResponse:
        try:
            start_time = datetime.now()
            logger.info(f"Starting processing of file: {file.filename}")
            
            # Validate file extension
            file_extension = file.filename.split('.')[-1].lower()
            if file_extension not in self.supported_extensions:
                raise DocumentProcessingError(f"Unsupported file extension: {file_extension}")

            # Validate file size (e.g., 10MB limit)
            file_content = await file.read()
            if len(file_content) > 10 * 1024 * 1024:
                raise DocumentProcessingError("File size exceeds 10MB limit")

            content = await self._process_file_by_type(file_extension, file_content)
            
            end_time = datetime.now()
            logger.info(f"Completed processing of file: {file.filename}")

            return ProcessingResponse(
                file_name=file.filename,
                content=content,
                processing_start_time=start_time,
                processing_end_time=end_time
            )

        except DocumentProcessingError as e:
            logger.error(f"Document processing error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}\n{traceback.format_exc()}")
            raise HTTPException(status_code=500, detail="Internal server error")

    async def _process_file_by_type(self, file_extension: str, file_content: bytes) -> str:
        try:
            if file_extension == 'txt':
                return file_content.decode('utf-8')
            elif file_extension in ['doc', 'docx']:
                return await self._process_word_document(file_content)
            elif file_extension == 'pdf':
                return await self._process_pdf_document(file_content)
        except Exception as e:
            logger.error(f"Error processing {file_extension} file: {str(e)}")
            raise DocumentProcessingError(f"Error processing {file_extension} file")

    async def _process_word_document(self, file_content):
        doc = Document(io.BytesIO(file_content))
        content = []

        # Extract text from paragraphs
        for paragraph in doc.paragraphs:
            content.append(paragraph.text)

        # Process tables if present
        for table in doc.tables:
            table_content = self.table_extractor.extract_word_table(table)
            content.append(table_content)

        # Process images if present
        for rel in doc.part.rels.values():
            if "image" in rel.target_ref:
                image_content = self.ocr_service.process_image(rel.target_part.blob)
                if image_content:
                    content.append(image_content)

        return "\n".join(content)

    async def _process_pdf_document(self, file_content):
        content = []
        pdf_file = PyPDF2.PdfReader(io.BytesIO(file_content))

        # Extract text from PDF
        for page in pdf_file.pages:
            content.append(page.extract_text())

        # Convert PDF to images and perform OCR if needed
        images = convert_from_bytes(file_content)
        for image in images:
            image_content = self.ocr_service.process_image(image)
            if image_content:
                content.append(image_content)

        return "\n".join(content) 