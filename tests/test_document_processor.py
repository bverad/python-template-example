import pytest
from fastapi.testclient import TestClient
from run import app
import os
from PIL import Image
import io

client = TestClient(app)

@pytest.fixture
def sample_files():
    # Create test files directory if it doesn't exist
    test_files_dir = "tests/test_files"
    os.makedirs(test_files_dir, exist_ok=True)
    
    # Create sample text file
    txt_path = os.path.join(test_files_dir, "sample.txt")
    with open(txt_path, "w") as f:
        f.write("Sample text content")

    # Create sample image with text
    img_path = os.path.join(test_files_dir, "sample_image.png")
    img = Image.new('RGB', (100, 30), color='white')
    img.save(img_path)

    return {
        'txt_path': txt_path,
        'img_path': img_path
    }

def test_process_txt_file(sample_files):
    with open(sample_files['txt_path'], "rb") as f:
        response = client.post(
            "/api/v1/process-document",
            files={"file": ("sample.txt", f, "text/plain")}
        )
    
    assert response.status_code == 200
    assert response.json()["file_name"] == "sample.txt"
    assert "Sample text content" in response.json()["content"]

def test_invalid_file_type():
    with open("tests/test_files/sample_image.png", "rb") as f:
        response = client.post(
            "/api/v1/process-document",
            files={"file": ("sample.png", f, "image/png")}
        )
    
    assert response.status_code == 400
    assert "Invalid file type" in response.json()["detail"]

def test_empty_file():
    response = client.post(
        "/api/v1/process-document",
        files={"file": ("empty.txt", b"", "text/plain")}
    )
    
    assert response.status_code == 400
    assert "Empty file" in response.json()["detail"]

def test_large_file():
    # Create a file larger than 10MB
    large_content = b"x" * (11 * 1024 * 1024)
    response = client.post(
        "/api/v1/process-document",
        files={"file": ("large.txt", large_content, "text/plain")}
    )
    
    assert response.status_code == 400
    assert "File size exceeds" in response.json()["detail"]

@pytest.mark.asyncio
async def test_concurrent_processing():
    """Test concurrent processing of multiple files"""
    import asyncio
    
    async def process_file():
        with open("tests/test_files/sample.txt", "rb") as f:
            return await client.post(
                "/api/v1/process-document",
                files={"file": ("sample.txt", f, "text/plain")}
            )
    
    # Process 5 files concurrently
    tasks = [process_file() for _ in range(5)]
    responses = await asyncio.gather(*tasks)
    
    for response in responses:
        assert response.status_code == 200

# Add more tests for PDF, DOC, and DOCX files 