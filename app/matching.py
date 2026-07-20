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
    return {
        "match_score": score,
        "matched_skills": skills["matched_skills"],
        "missing_skills": skills["missing_skills"]
    }




if __name__ == "__main__":
    # Тест 1: исходный пример
    resume_1 = "Python pandas scikit-learn FastAPI"

    job_1 = "Python SQL Docker FastAPI ML pipelines"

    result1 = create_match_result(resume_1, job_1)

    print(result1)


    # Тест 2: полное совпадение
    resume_2 = "Python SQL Docker FastAPI"

    job_2 = "Python SQL Docker FastAPI"

    result2 = create_match_result(resume_2, job_2)

    print(result2)


    # Тест 3: частичное совпадение
    resume_3 = "Python pandas FastAPI"

    job_3 = "Python SQL Docker FastAPI"

    result3 = create_match_result(resume_3, job_3)

    print(result3)


    # Тест 4: нет совпадений
    resume_4 = "Python pandas numpy"

    job_4 = "AutoCAD construction architecture"

    result4 = create_match_result(resume_4, job_4)

    print(result4)

