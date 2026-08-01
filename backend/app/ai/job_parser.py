import re

COMMON_SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "PHP",
    "Laravel",
    "React",
    "Next.js",
    "Vue",
    "Angular",
    "Node.js",
    "Express",
    "FastAPI",
    "Django",
    "Flask",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "SQLite",
    "Docker",
    "Git",
    "GitHub",
    "Linux",
    "HTML",
    "CSS",
    "Tailwind",
    "Bootstrap",
    "REST API",
    "GraphQL",
    "Redis",
    "AWS",
    "Azure",
    "Kubernetes",
    "CI/CD",
]

# ====================================================
# PUT THIS BELOW COMMON_SKILLS
# ====================================================

EXPERIENCE_PATTERNS = [
    r"(\d+)\+?\s+years?\s+of\s+experience",
    r"minimum\s+of\s+(\d+)\s+years?",
    r"at\s+least\s+(\d+)\s+years?",
]

EDUCATION = [
    "Bachelor",
    "Master",
    "PhD",
    "BSIT",
    "Computer Science",
    "Information Technology",
]

WORK_TYPES = ["Remote", "Hybrid", "On-site"]

LEVELS = ["Intern", "Junior", "Mid", "Senior", "Lead"]


def parse_job(text: str):

    result = {
        "skills": [],
        "experience": [],
        "education": [],
        "work_type": [],
        "level": [],
    }

    lower = text.lower()

    for skill in COMMON_SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, lower):
            result["skills"].append(skill)

    for pattern in EXPERIENCE_PATTERNS:
        matches = re.findall(pattern, lower)
        result["experience"].extend(matches)

    for item in EDUCATION:
        if item.lower() in lower:
            result["education"].append(item)

    for item in WORK_TYPES:
        if item.lower() in lower:
            result["work_type"].append(item)

    for item in LEVELS:
        if item.lower() in lower:
            result["level"].append(item)

    return result
