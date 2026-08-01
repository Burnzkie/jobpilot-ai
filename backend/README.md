# 🚀 JobPilot AI

AI-powered backend for **JobPilot AI**, a job application management system that helps users organize job applications, upload resumes, generate AI-assisted cover letters, and discover suitable job opportunities.

---

## ✨ Features

### 🔐 Authentication
- User registration
- User login
- JWT authentication
- Password hashing using bcrypt

### 💼 Job Management
- Save jobs
- Update jobs
- Delete jobs
- Search jobs
- Pagination
- Filter by company
- Filter by status

### 📄 Resume Management
- Upload resume
- Retrieve uploaded resumes
- Get latest resume
- Resume validation

### 📌 Job Applications
- Save application
- Update application status
- Add notes
- Delete application
- Prevent duplicate applications

### 🤖 AI Features
- AI Cover Letter Generation
- Resume Parsing
- Job Matching
- Skill Matching
- Recommendation Engine

### 🧪 Testing
- Repository Tests
- Service Tests
- API Tests

**61 Passing Tests**

---

# 🏗 Architecture

```
                Client

                   │

                   ▼

        FastAPI Routers (API)

                   │

                   ▼

              Services

                   │

                   ▼

           Repository Layer

                   │

                   ▼

              SQLAlchemy

                   │

                   ▼

             PostgreSQL
```

---

# 📂 Project Structure

```
app
│
├── ai
├── api
├── auth
├── constants
├── core
├── database
├── dependencies
├── middleware
├── models
├── providers
├── repositories
├── scheduler
├── schemas
├── scrapers
├── services
└── utils
```

---

# 🛠 Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT
- Docker
- Pytest
- GitHub Actions

---

# ⚙ Installation

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/jobpilot-ai.git
```

Go to backend

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

# ▶ Run Development Server

```bash
uvicorn app.main:app --reload
```

Open

```
http://localhost:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

# 🧪 Testing

Run all tests

```bash
pytest
```

Coverage

```bash
pytest --cov=app
```

---

# 📚 API Documentation

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 🔄 CI/CD

GitHub Actions automatically runs:

- Unit Tests
- API Tests
- Flake8

on every push.

---

# 📌 Main Endpoints

## Authentication

```
POST /api/auth/register
POST /api/auth/login
```

---

## Jobs

```
POST /api/jobs
GET /api/jobs
GET /api/jobs/{id}
PUT /api/jobs/{id}
DELETE /api/jobs/{id}
POST /api/jobs/import
```

---

## Resume

```
POST /api/resumes/upload
GET /api/resumes
GET /api/resumes/latest
```

---

## Applications

```
POST /api/applications
GET /api/applications
PUT /api/applications/{id}
DELETE /api/applications/{id}
```

---

## Cover Letter

```
POST /api/cover-letter
```

---

# 🔒 Authentication

Protected endpoints require

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 📈 Current Progress

| Module | Status |
|---------|--------|
| Authentication | ✅ |
| Jobs CRUD | ✅ |
| Resume Upload | ✅ |
| Job Applications | ✅ |
| AI Cover Letter | ✅ |
| AI Matching | ✅ |
| Repository Layer | ✅ |
| Service Layer | ✅ |
| API Layer | ✅ |
| Unit Tests | ✅ |
| Docker | ✅ |
| GitHub Actions | ✅ |

---

# 🚀 Future Improvements

- Refresh Token
- Email Verification
- Password Reset
- Redis Cache
- Background Jobs
- Interview Question Generator
- Job Recommendation Improvements
- WebSocket Notifications

---

# 👨‍💻 Author

Developed by **Jude Delantes Burnea**

Bachelor of Science in Information Technology

Philippine Advent College