# Document Processing Service

## Overview
This service is a REST API that processes various document types (PDF, DOC, DOCX, TXT) and extracts text content from them. It can handle:
- Plain text documents
- Documents with tables
- Documents with embedded images (using OCR)

## Features
- Text extraction from multiple document formats
- Table detection and processing
- OCR processing for embedded images
- Async processing for better performance
- Comprehensive error handling
- Detailed logging
- Docker support
- API documentation via Swagger/OpenAPI

## Installation

### Prerequisites
- Python 3.10+
- Tesseract OCR
- Poppler Utils (for PDF processing)
- Docker (optional)

### System Dependencies

### Ubuntu/Debian
```
sudo apt-get update
sudo apt-get install -y tesseract-ocr poppler-utils
```

### MacOS
```
brew install tesseract poppler
```

### Local Setup

1. Clone the repository:
```
git clone <repository-url>
cd document-processor
```

2. Create and activate virtual environment:
```
python -m venv venv
source venv/bin/activate # Linux/MacOS
venv\Scripts\activate # Windows
```

3. Install Python dependencies:
```
pip install -r requirements.txt
```

### Docker Setup
1. Build the Docker image:
```
docker build -t document-processor .
```

2. Run the container:
```
docker run -p 8000:8000 document-processor
```

## Usage

### Starting the Service

### Local development
```
uvicorn run:app --reload --host 0.0.0.0 --port 8000
```

### Production
```
uvicorn run:app --host 0.0.0.0 --port 8000 --workers 4
```

### API Endpoints

#### Process Document
```
POST /api/v1/process-document
```


Example using curl:
```
curl -X POST "http://localhost:8000/api/v1/process-document" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@/path/to/document.pdf"
```


Example Response:
```
json
{
"file_name": "document.pdf",
"content": "Extracted text content...",
"processing_start_time": "2024-01-01T12:00:00",
"processing_end_time": "2024-01-01T12:00:01"
}
```

### API Documentation

Access the Swagger documentation at: `http://localhost:8000/docs`

## Configuration

### Environment Variables
- `MAX_FILE_SIZE`: Maximum file size in bytes (default: 10MB)
- `LOG_LEVEL`: Logging level (default: INFO)
- `PORT`: Server port (default: 8000)

### Logging Configuration
Logs are stored in the `logs` directory:
- `document_processor.log`: Main application log
- Logs rotate at 10MB with 5 backup files
- Format: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`

## Testing

### Running Tests

Run all tests
```
pytest
```

Run with coverage report
```
pytest --cov=app tests/
```

Run specific test file
```
pytest tests/test_document_processor.py
```

### Test Coverage
The test suite includes:
- Unit tests for document processing
- Integration tests for API endpoints
- Concurrent processing tests
- Error handling tests
- File type validation tests

## Security Considerations

### Input Validation
- File type validation
- File size limits (10MB default)
- Content type verification
- Secure file handling

### System Security
- All dependencies are pinned to specific versions
- Regular security updates via Docker base image
- Temporary file cleanup
- Error message sanitization

### API Security
- Rate limiting (recommended for production)
- Input sanitization
- Secure error handling
- CORS configuration (if needed)

## Performance Notes

### Optimization Features
- Asynchronous processing
- Efficient file handling
- Memory usage optimization
- Logging rotation

### Performance Tips
1. Concurrent Processing:
   - Service handles multiple requests concurrently
   - Uses FastAPI's async capabilities
   - Configurable worker count

2. Resource Management:
   - Automatic cleanup of temporary files
   - Memory-efficient file processing
   - Streaming file uploads

3. Scaling Considerations:
   - Horizontal scaling via Docker
   - Load balancing support
   - Stateless architecture

### Known Limitations
- Maximum file size: 10MB
- Supported file types: PDF, DOC, DOCX, TXT
- OCR processing time varies with image quality
- Memory usage increases with file size

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License