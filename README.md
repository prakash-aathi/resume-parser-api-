# Resume Parser API (using FastAPI + OpenAI + Langchain)

This project parses resumes to extract personal info, education, skills, projects, certifications, languages, awards, and more using OpenAI's GPT model (`gpt-4o`).

---

## 🚀 Features

- Upload PDF or DOCX resume
- Extract structured data using AI (LLM)
- FastAPI backend
- Multiple endpoints based on priority
- Logs, metadata (token count, processing time, cost estimate)
- Supports deployment to production (e.g., AWS)

---

## 🧰 Installation

### 1. Clone the project

```bash
git clone https://github.com/your-username/resume-parser.git
cd resume-parser
```

2. Create a virtual environment
   
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

3. Install requirements
pip install -r requirements.txt


📦 .env File
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here

▶️ How to Start the API
uvicorn app.main:app --reload
Once running, you can test your APIs at:

📄 Swagger UI:
http://localhost:8000/docs


 API Endpoints
/parse-resume
Extracts: personal info, skills, education

/parse-second-priority
Extracts: projects, certifications, awards, languages

/parse-third-priority
Extracts: memberships, training, skilling, conference

Each returns:

structured JSON

metadata like token usage, character count, estimated cost, and processing time

🚀 Deployment (Basic Setup)
 Run on EC2 or Any Server
Install Python, Git

Clone repo, setup virtualenv

Install requirements

Run with:

uvicorn app.main:app --host 0.0.0.0 --port 80
