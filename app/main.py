from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from app.parser import extract_text
from app.llm import extract_personal_info, extract_training
from app.llm import extract_skills, extract_memberships
from app.llm import extract_education, extract_languages
from app.llm import extract_employment_history, extract_awards
from app.llm import extract_projects, extract_certifications
from app.llm import extract_skilling, extract_conferences
from app.utils import count_tokens, estimate_cost

from fastapi import UploadFile, File, HTTPException
from app.parser import extract_text
from app.llm import (
    extract_memberships,
    extract_training,
    extract_skilling,
    extract_conferences
)

import time
from datetime import datetime

app = FastAPI()

@app.post("/parse-resume")
async def parse_resume_important_info(file: UploadFile = File(...)):
    start_time = time.time()  # start timer

    file_ext = file.filename.split(".")[-1].lower()
    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

    temp_file_path = f"temp_upload.{file_ext}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        raw_text = extract_text(temp_file_path, file_ext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(temp_file_path)

    personal_info = await extract_personal_info(raw_text)
    skills = await extract_skills(raw_text)
    education =await extract_education(raw_text)
    employment = await extract_employment_history(raw_text)

    char_count = len(raw_text)
    token_count = count_tokens(raw_text, model_name="gpt-4o")
    cost_estimate = estimate_cost(token_count)
    processing_time = round(time.time() - start_time, 2)  # in seconds
    timestamp = datetime.utcnow().isoformat() + "Z"  # current UTC time

    return {
        "personal_info": personal_info,
        "skills": skills,
        "education": education,
        "employment": employment,
        "raw_text_preview": raw_text[:1000],
         "meta": {
            "char_count": char_count,
            "token_count": token_count,
            "estimated_cost_usd": cost_estimate,
            "processing_time_seconds": processing_time,
            "model_used": "gpt-4o",
            "timestamp": timestamp
        }
    }





@app.post("/parse-second-priority")
async def parse_projects_and_certs(file: UploadFile = File(...)):
    start_time = time.time()  # start timer

    file_ext = file.filename.split(".")[-1].lower()
    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

    temp_file_path = f"temp_upload.{file_ext}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        raw_text = extract_text(temp_file_path, file_ext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(temp_file_path)

    projects = await extract_projects(raw_text)
    certifications = await extract_certifications(raw_text)
    awards = await extract_awards(raw_text)
    languages = await extract_languages(raw_text)
    

    # meta 
    char_count = len(raw_text)
    token_count = count_tokens(raw_text, model_name="gpt-4o")
    cost_estimate = estimate_cost(token_count)
    processing_time = round(time.time() - start_time, 2)  # in seconds
    timestamp = datetime.utcnow().isoformat() + "Z"  # current UTC time

    return {
        "projects": projects,
        "certifications": certifications,
        "awards": awards,
        "extract_languages": languages,
        "raw_text_preview": raw_text[:1000],
        "meta": {
            "char_count": char_count,
            "token_count": token_count,
            "estimated_cost_usd": cost_estimate,
            "processing_time_seconds": processing_time,
            "model_used": "gpt-4o",
            "timestamp": timestamp
        }
    }


@app.post("/parse-third-priority")
async def parse_membership_training_skilling_conference(file: UploadFile = File(...)):
    start_time = time.time()  # start timer

    file_ext = file.filename.split(".")[-1].lower()
    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

    temp_file_path = f"temp_upload.{file_ext}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        raw_text = extract_text(temp_file_path, file_ext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(temp_file_path)

    # Resume processing
    memberships = await extract_memberships(raw_text)
    training = await extract_training(raw_text)
    skilling = await extract_skilling(raw_text)
    conferences = await extract_conferences(raw_text)

    # Metadata
    char_count = len(raw_text)
    token_count = count_tokens(raw_text, model_name="gpt-4o")
    cost_estimate = estimate_cost(token_count)
    processing_time = round(time.time() - start_time, 2)  # in seconds
    timestamp = datetime.utcnow().isoformat() + "Z"  # current UTC time

    return {
        "memberships": memberships,
        "training": training,
        "skilling": skilling,
        "conferences": conferences,
        "raw_text_preview": raw_text[:1000],
        "meta": {
            "char_count": char_count,
            "token_count": token_count,
            "estimated_cost_usd": cost_estimate,
            "processing_time_seconds": processing_time,
            "model_used": "gpt-4o",
            "timestamp": timestamp
        }
    }
