from pydantic import BaseModel
from datetime import datetime

class ProcessingResponse(BaseModel):
    file_name: str
    content: str
    processing_start_time: datetime
    processing_end_time: datetime 