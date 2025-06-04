import fitz  # PyMuPDF
import docx
from typing import Union
from pathlib import Path

def extract_text(file_path: Union[str, Path], file_type: str) -> str:
    if file_type == "pdf":
        return extract_text_from_pdf(file_path)
    elif file_type == "docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

def extract_text_from_pdf(file_path: Union[str, Path]) -> str:
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path: Union[str, Path]) -> str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])
