import os
import fitz
from docx import Document

from src.logger.logger import logging
from src.exception.custom_exception import CustomException
import sys
from src.utils.text_cleaner import clean_text

class ResumeParser:
    """Handles resume text extraction from PDF and DOCX files"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text_from_pdf(self) -> str:
        """Extract text from PDF file"""

        try:
            logging.info("Entered PDF text extraction method")

            text = ""

            pdf_document = fitz.open(self.file_path)

            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text += page.get_text()

            logging.info("PDF text extraction completed")

            return text
        
        except Exception as e:
            logging.error("Error occured during PDF extraction")
            raise CustomException(e, sys)
        

    def extract_text_from_docx(self) -> str:
        """Extract text from DOCX file"""

        try:
            logging.info("Entered DOCX text extraction method")

            doc = Document(self.file_path)

            text = "\n".join(
                [paragraph.text for paragraph in doc.paragraphs]
            )

            logging.info("DOCX text extraction completed")

            return text
        
        except Exception as e:
            logging.error("Error occured during DOCX extraction")
            raise CustomException(e, sys)
        

    def extract_resume_text(self) -> str:
        """Detect file type and extracted text"""

        try:
            logging.info("Entered resume extraction pipeline")

            file_extension = os.path.splitext(self.file_path)[1].lower()

            if file_extension == ".pdf":
                text = self.extract_text_from_pdf()
                return clean_text(text)
            
            elif file_extension == ".docx":
                text = self.extract_text_from_docx()
                return clean_text(text)
            
            else:
                raise Exception(
                    "Unsupported file format. Only PDF and DOCX are supported."
                )
            
        except Exception as e:
            logging.error("Error in resume extraction pipeline")
            raise CustomException(e, sys)