def skill_match(resume_skills, job_skills):

    resume = {skill.lower() for skill in resume_skills}

    job = {skill.lower() for skill in job_skills}

    matched = resume.intersection(job)

    missing = job.difference(resume)

    if len(job) == 0:
        score = 100
    else:
        score = round(len(matched) / len(job) * 100, 2)

    return {"score": score, "matched": sorted(matched), "missing": sorted(missing)}
