
SKILLS = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "fastapi",
    "docker",
    "git",
    "github",
    "pytest",
    "linux",
    "aws",
    "azure",
    "postgresql",
    "mongodb",
    "tensorflow",
    "pytorch",
]

def extract_skills(text:str) -> set:
    clean_text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        if skill in clean_text:
            found_skills.add(skill)
    
    return found_skills

def compare_skills(resume_text:str, job_description:str) -> dict:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = resume_skills.intersection(job_skills)

    missing_skills = job_skills.difference(resume_skills)

    return {
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }