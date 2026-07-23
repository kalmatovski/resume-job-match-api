from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.skills import compare_skills

def preprocess_text(text:str) -> str:
    text = text.lower()
    text = " ".join(text.split())
    return text

def calculate_match_score(resume_text:str,job_description:str, debug:bool = False) -> float:
    clean_resume = preprocess_text(resume_text)
    clean_job = preprocess_text(job_description)

    vectorizer = TfidfVectorizer()

    text_vectors = vectorizer.fit_transform(
        [clean_resume, clean_job]
    )

    if debug:
        features = vectorizer.get_feature_names_out()
        print("TF-IDF features:", features)

    resume_vector = text_vectors[0]

    job_vector = text_vectors[1]

    similarity = cosine_similarity(
        resume_vector,
        job_vector
    )[0][0]

    return round(float(similarity), 3)

def create_match_result(resume:str, job:str) -> dict:
    score = calculate_match_score(resume_text=resume, job_description=job)
    skills = compare_skills(resume,job)
    fit_level = get_fit_level(score)
    recommendation = create_recommendation(fit_level=fit_level, missing_skills=skills["missing_skills"])
    return {
        "match_score": score,
        "matched_skills": skills["matched_skills"],
        "missing_skills": skills["missing_skills"],
        "fit_level":fit_level,
        "recommendation":recommendation
    }


def get_fit_level(match_score:float)->str:
    if match_score >=0.60:
        return "high"
    elif match_score >=0.30:
        return "medium"
    else:
        return "low"


def create_recommendation(
    fit_level: str,
    missing_skills: list[str]
) -> str:
    # Если отсутствующих навыков нет
    if not missing_skills:
        return "Strong match. All detected job skills are covered."

    skills_text = ", ".join(missing_skills)

    if len(missing_skills) == 1:
        skill_label = "this skill"
    else:
        skill_label = "these skills"

    return (
        f"{fit_level.capitalize()} match. "
        f"Improve {skill_label}: {skills_text}."
    )