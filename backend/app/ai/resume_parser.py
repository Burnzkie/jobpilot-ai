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
]


def parse_resume(text: str):

    result = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "education": [],
        "experience": [],
    }

    # Email
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    if email:
        result["email"] = email.group()

    # Phone
    phone = re.search(r"(\+?\d[\d\s\-]{8,15})", text)

    if phone:
        result["phone"] = phone.group()

    # Skills
    text_lower = text.lower()

    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            result["skills"].append(skill)

    # Name (simple assumption: first non-empty line)
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines:
        result["name"] = lines[0]

    return result
