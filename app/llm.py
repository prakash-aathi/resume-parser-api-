import os
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from enum import Enum


load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Sub-models
class DateOfBirth(BaseModel):
    date: Optional[str] = Field(description="Day of birth, like '12'")
    month: Optional[str] = Field(description="Month of birth, like 'May'")
    year: Optional[str] = Field(description="Year of birth, like '1990'")

class SocialUrls(BaseModel):
    linkedin: Optional[str] = Field(description="LinkedIn profile URL")
    github: Optional[str] = Field(description="GitHub profile URL")

class MobileNumber(BaseModel):
    countryCode: Optional[str] = Field(description="Country code like +1 or +91")
    number: Optional[str] = Field(description="Phone number without country code")

class PersonalInfo(BaseModel):
    firstName: Optional[str] = Field(description="First name of the person")
    lastName: Optional[str] = Field(description="Last name of the person")
    email: Optional[str] = Field(description="Email address")
    mobileNumber: Optional[MobileNumber] = Field(description="Phone number with country code split")
    dateOfBirth: Optional[DateOfBirth] = Field(description="Date of birth as an object")
    address: Optional[str] = Field(description="Full address")
    country: Optional[str] = Field(description="Country")
    state: Optional[str] = Field(description="State")
    city: Optional[str] = Field(description="City")
    postalCode: Optional[str] = Field(description="Postal code or ZIP")
    about: Optional[str] = Field(description="About or summary section from resume")
    socialUrls: Optional[SocialUrls] = Field(description="Social profile URLs")

class SkillsItem(BaseModel):
    skill: str = Field(description="Skill name like Python, Excel, etc.")
    occupation: str = Field(description="Occupation or job title this skill relates to (e.g. Software Developer)")

class DateObject(BaseModel):
    date: Optional[str] = Field(description="Day of the month like '01'")
    month: Optional[str] = Field(description="Month like 'August'")
    year: Optional[str] = Field(description="Year like '2019'")

class EducationItem(BaseModel):
    institution: str = Field(description="Name of the educational institution")
    course: str = Field(description="Degree or course studied")
    location: Optional[str] = Field(description="City and country of the institution")
    startDate: Optional[DateObject] = Field(description="Start date of the course")
    endDate: Optional[DateObject] = Field(description="End date of the course")
    description: Optional[str] = Field(description="Details of coursework or achievements")

# Employment type enum
class EmploymentType(str, Enum):
    full_time = "full_time"
    part_time = "part_time"
    freelance = "freelance"
    internship = "internship"
    own = "own"

class EmploymentItem(BaseModel):
    organizationName: str = Field(description="Name of the company or organization")
    durationInMonths: Optional[int] = Field(description="Duration of employment in months")
    type: EmploymentType = Field(description="Type of employment, one of: full_time, part_time, freelance, internship, own")
    location: Optional[str] = Field(description="Location of the organization")
    startDate: Optional[DateObject] = Field(description="Start date of the employment")
    endDate: Optional[DateObject] = Field(description="End date of the employment")
    jobTitle: Optional[str] = Field(description="Job title or position held")

# Enum for project type
class ProjectType(str, Enum):
    own = "own"
    employment = "employment"
    academic = "academic"

class ProjectItem(BaseModel):
    projectName: str = Field(description="Name of the project")
    startDate: Optional[DateObject] = Field(description="Start date of the project")
    endDate: Optional[DateObject] = Field(description="End date of the project")
    durationInMonths: Optional[int] = Field(description="Duration of the project in months")
    description: Optional[str] = Field(description="Brief summary of the project")
    organizationName: Optional[str] = Field(description="Name of the organization where project was done")
    location: Optional[str] = Field(description="Location where the project was done")
    type: ProjectType = Field(description="Type of project: own, employment, or academic")

class CertificationItem(BaseModel):
    certificationName: str = Field(description="Name of the certification")
    organizationName: Optional[str] = Field(description="Issuing organization name")
    location: Optional[str] = Field(description="Location of the organization")
    startDate: Optional[DateObject] = Field(description="Start date of the certification course")
    endDate: Optional[DateObject] = Field(description="End date of the certification course")
    durationInMonths: Optional[int] = Field(description="Duration in months")
    description: Optional[str] = Field(description="Details or summary of the certification")

class AwardItem(BaseModel):
    awardName: str = Field(description="Name of the award")
    location: Optional[str] = Field(description="Location where the award was received")
    givenDate: Optional[DateObject] = Field(description="Date the award was received")
    description: Optional[str] = Field(description="Description of the award or its context")

class LanguageItem(BaseModel):
    language: str = Field(description="Language name")
    read: Optional[bool] = Field(description="Can the user read this language?")
    write: Optional[bool] = Field(description="Can the user write this language?")
    speak: Optional[bool] = Field(description="Can the user speak this language?")

class MembershipItem(BaseModel):
    organization: str = Field(description="Name of the membership organization")
    durationInMonths: Optional[int] = Field(description="Duration of membership in months")
    location: Optional[str] = Field(description="Location of the organization")
    description: Optional[str] = Field(description="Details about the membership")

class TrainingItem(BaseModel):
    trainingName: str = Field(description="Name of the training program")
    organization: Optional[str] = Field(description="Organization that conducted the training")
    location: Optional[str] = Field(description="Location of the training")
    startDate: Optional[DateObject] = Field(description="Training start date")
    endDate: Optional[DateObject] = Field(description="Training end date")

class SkillingItem(BaseModel):
    skillingName: str = Field(description="Name of the skill acquired or course")
    organization: Optional[str] = Field(description="Organization providing the skill training")
    location: Optional[str] = Field(description="Location of the skill training")
    startDate: Optional[DateObject] = Field(description="Start date of skilling")
    endDate: Optional[DateObject] = Field(description="End date of skilling")
    description: Optional[str] = Field(description="Additional details about the skilling")
    durationInMonths: Optional[int] = Field(description="Total duration in months")

class ConferenceItem(BaseModel):
    conferenceName: str = Field(description="Name of the conference")
    organization: Optional[str] = Field(description="Organizing body")
    location: Optional[str] = Field(description="Conference location")
    startDate: Optional[DateObject] = Field(description="Start date of the conference")
    endDate: Optional[DateObject] = Field(description="End date of the conference")
    description: Optional[str] = Field(description="Details about the conference")
    durationInMonths: Optional[int] = Field(description="Duration of the conference in months")


award_parser = JsonOutputParser(pydantic_object=AwardItem)

award_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\n"
        "From the resume text, extract a list of awards or honors received by the person. For each award, include:\n"
        "- awardName\n"
        "- location\n"
        "- givenDate (object: date, month, year)\n"
        "- description\n\n"
        "Format the output as a JSON list.\n\n"
        "{format_instructions}\n\n"
        "Resume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": award_parser.get_format_instructions()}
)

award_chain = award_prompt | llm | award_parser


# Parser
certification_parser = JsonOutputParser(pydantic_object=CertificationItem)

# Prompt
certification_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\n"
        "From the resume text, extract certification details. For each certification, return:\n"
        "- certificationName\n"
        "- organizationName\n"
        "- location\n"
        "- startDate (object: date, month, year)\n"
        "- endDate (object: date, month, year)\n"
        "- durationInMonths\n"
        "- description\n\n"
        "Return a JSON list of such objects.\n\n"
        "{format_instructions}\n\n"
        "Resume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": certification_parser.get_format_instructions()}
)

certification_chain = certification_prompt | llm | certification_parser


# Parser
project_parser = JsonOutputParser(pydantic_object=ProjectItem)

# Prompt
project_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\n"
        "From the resume text, extract details about projects. For each project, return:\n"
        "- projectName\n"
        "- startDate (object: date, month, year)\n"
        "- endDate (object: date, month, year)\n"
        "- durationInMonths\n"
        "- description\n"
        "- organizationName\n"
        "- location\n"
        "- type (only one of: own, employment, academic)\n\n"
        "Return a JSON list of such objects.\n\n"
        "{format_instructions}\n\n"
        "Resume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": project_parser.get_format_instructions()}
)

project_chain = project_prompt | llm | project_parser


# Parser
parser = JsonOutputParser(pydantic_object=PersonalInfo)

# Prompt
prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\n"
        "Extract the following personal information from the resume text:\n"
        "- firstName, lastName\n"
        "- email\n"
        "- mobileNumber (as object: countryCode, number)\n"
        "- dateOfBirth (as object: date, month, year)\n"
        "- address, country, state, city, postalCode\n"
        "- about\n"
        "- socialUrls (as object: linkedin, github)\n\n"
        "{format_instructions}\n\n"
        "Resume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Chain
chain = prompt | llm | parser

# Parser for skills
skills_parser = JsonOutputParser(pydantic_object=SkillsItem)

# Prompt for extracting skill-occupation pairs
skills_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\n"
        "From the resume text, extract a list of skills and their corresponding occupations.\n"
        "Each item should be a pair of:\n"
        "- skill (e.g., Python)\n"
        "- occupation (e.g., Software Developer)\n\n"
        "{format_instructions}\n\n"
        "Resume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": skills_parser.get_format_instructions()}
)

skills_chain = skills_prompt | llm | skills_parser



# Parser
education_parser = JsonOutputParser(pydantic_object=EducationItem)

# Prompt
education_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\n"
        "From the resume text, extract all education details. For each entry, provide:\n"
        "- institution\n"
        "- course (degree or program)\n"
        "- location\n"
        "- startDate (object: date, month, year)\n"
        "- endDate (object: date, month, year)\n"
        "- description\n\n"
        "Format output as a JSON list.\n\n"
        "{format_instructions}\n\n"
        "Resume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": education_parser.get_format_instructions()}
)

education_chain = education_prompt | llm | education_parser


# Parser and prompt
employment_parser = JsonOutputParser(pydantic_object=EmploymentItem)

employment_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\n"
        "From the resume text, extract the employment history. For each job, provide:\n"
        "- organizationName\n"
        "- durationInMonths\n"
        "- type (only one of: full_time, part_time, freelance, internship, own)\n"
        "- location\n"
        "- startDate (object: date, month, year)\n"
        "- endDate (object: date, month, year)\n"
        "- jobTitle\n\n"
        "Format output as a JSON list.\n\n"
        "{format_instructions}\n\n"
        "Resume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": employment_parser.get_format_instructions()}
)

employment_chain = employment_prompt | llm | employment_parser

# === Languages Known ===
language_parser = JsonOutputParser(pydantic_object=LanguageItem)
language_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\nFrom the resume text, extract languages the person knows. For each language, return:\n"
        "- language\n- read (true/false)\n- write (true/false)\n- speak (true/false)\n\n"
        "{format_instructions}\n\nResume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": language_parser.get_format_instructions()}
)
language_chain = language_prompt | llm | language_parser


# === Memberships ===
membership_parser = JsonOutputParser(pydantic_object=MembershipItem)
membership_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\nExtract details about professional or academic memberships. For each, include:\n"
        "- organization\n- durationInMonths\n- location\n- description\n\n"
        "{format_instructions}\n\nResume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": membership_parser.get_format_instructions()}
)
membership_chain = membership_prompt | llm | membership_parser


# === Training ===
training_parser = JsonOutputParser(pydantic_object=TrainingItem)
training_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\nExtract training programs attended. For each one, return:\n"
        "- trainingName\n- organization\n- location\n- startDate (date/month/year)\n- endDate (date/month/year)\n\n"
        "{format_instructions}\n\nResume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": training_parser.get_format_instructions()}
)
training_chain = training_prompt | llm | training_parser


# === Skilling ===
skilling_parser = JsonOutputParser(pydantic_object=SkillingItem)
skilling_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\nFrom the resume text, extract skills learned through training. For each skill, include:\n"
        "- skillingName\n- organization\n- location\n- startDate\n- endDate\n- description\n- durationInMonths\n\n"
        "{format_instructions}\n\nResume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": skilling_parser.get_format_instructions()}
)
skilling_chain = skilling_prompt | llm | skilling_parser


# === Conferences ===
conference_parser = JsonOutputParser(pydantic_object=ConferenceItem)
conference_prompt = PromptTemplate(
    template=(
        "You are a resume parser.\n\nExtract all conferences attended. For each, include:\n"
        "- conferenceName\n- organization\n- location\n- startDate\n- endDate\n- description\n- durationInMonths\n\n"
        "{format_instructions}\n\nResume text:\n{resume_text}"
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": conference_parser.get_format_instructions()}
)
conference_chain = conference_prompt | llm | conference_parser





# Function to call in FastAPI
async def extract_personal_info(resume_text: str) -> dict:
    result = await chain.ainvoke({"resume_text": resume_text})
    return result


async def extract_skills(resume_text: str) -> list[dict]:
    results = []
    # Since the parser expects 1 object per call, we’ll call it multiple times or parse JSON list from LLM
    # Better way: ask LLM to return a full list matching the schema
    prompt = (
        "Extract a list of skills and map each skill to the most relevant occupation title (like in O*NET).\n"
        "Return a list of objects like this:\n"
        "[{\"skill\": \"Python\", \"occupation\": \"Software Developer\"}, ...]\n\n"
        f"Resume text:\n{resume_text}"
    )
    full_prompt = PromptTemplate(
        template="{format_instructions}\n\n{resume_text}",
        input_variables=["resume_text"],
        partial_variables={"format_instructions": skills_parser.get_format_instructions()}
    )
    chain = full_prompt | llm | skills_parser
    result = await chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result


async def extract_education(resume_text: str) -> list[dict]:
    result = await education_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result

async def extract_employment_history(resume_text: str) -> list[dict]:
    result = await employment_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result

# Async function
async def extract_projects(resume_text: str) -> list[dict]:
    result = await project_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result

# Async function
async def extract_certifications(resume_text: str) -> list[dict]:
    result = await certification_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result

async def extract_awards(resume_text: str) -> list[dict]:
    result = await award_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result

async def extract_languages(resume_text: str) -> list[dict]:
    result = await language_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result


async def extract_memberships(resume_text: str) -> list[dict]:
    result = await membership_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result


async def extract_training(resume_text: str) -> list[dict]:
    result = await training_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result


async def extract_skilling(resume_text: str) -> list[dict]:
    result = await skilling_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result


async def extract_conferences(resume_text: str) -> list[dict]:
    result = await conference_chain.ainvoke({"resume_text": resume_text})
    return [result] if isinstance(result, dict) else result
