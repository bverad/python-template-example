import pytesseract
from PIL import Image
import io

class OCRService:
    def process_image(self, image_data):
        """
        Process image data using OCR to extract text.
        """
        if isinstance(image_data, bytes):
            image = Image.open(io.BytesIO(image_data))
        else:
            image = image_data

        try:
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            print(f"OCR processing error: {str(e)}")
            return "" 