from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text:str) -> str:
    text = text.lower()
    text = "".join(text.split())
    return text

def calculate_match_score(resume_text:str,job_description:str) -> float:
    clean_resume = preprocess_text(resume_text)
    clean_job = preprocess_text(job_description)

    vectorizer = TfidfVectorizer()

    text_vectors = vectorizer.fit_transform(
        [clean_resume, clean_job]
    )
    print("TF-IDF features:", vectorizer.get_feature_names_out())

    resume_vector = text_vectors[0]

    job_vector = text_vectors[1]

    similarity = cosine_similarity(
        resume_vector,
        job_vector
    )[0][0]

    match_score = round(float(similarity), 3)

    return match_score


if __name__ == "__main__":
    resume = """
    Python, pandas, scikit-learn, FastAPI
"""
    job_description = """
    Python, SQL, Docker, FastAPI, ML piplines
"""
    score = calculate_match_score(
        resume_text=resume,
        job_description=job_description
    )

    print("Match score 1:", score)

    resume2 = "Python SQL Docker FastAPI"
    job_description2= "Python SQL Docker FastAPI"

    score2 = calculate_match_score(
        resume_text=resume2,
        job_description=job_description2
    )

    print("Match score 2:", score2)


    resume3 = "Python pandas FastAPI"
    job_description3 = "Python SQL Docker FastAPI"

    score3 = calculate_match_score(
        resume_text=resume3,
        job_description=job_description3
    )

    print("Match score 3:", score3)

    
    resume4 = "Python pandas numpy"
    job_description4 = "AutoCAD construction architecture"

    score4 = calculate_match_score(
        resume_text=resume4,
        job_description=job_description4
    )



    print("Match score 4:", score4)

