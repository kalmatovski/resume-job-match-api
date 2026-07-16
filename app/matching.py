from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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


if __name__ == "__main__":
    # Тест 1: исходный пример
    resume_1 = "Python pandas scikit-learn FastAPI"

    job_1 = "Python SQL Docker FastAPI ML pipelines"

    score_1 = calculate_match_score(resume_1, job_1, debug=True)

    print("Match score 1:", score_1)
    print()


    # Тест 2: полное совпадение
    resume_2 = "Python SQL Docker FastAPI"

    job_2 = "Python SQL Docker FastAPI"

    score_2 = calculate_match_score(resume_2, job_2,debug=True)

    print("Match score 2:", score_2)
    print()


    # Тест 3: частичное совпадение
    resume_3 = "Python pandas FastAPI"

    job_3 = "Python SQL Docker FastAPI"

    score_3 = calculate_match_score(resume_3, job_3, debug=True)

    print("Match score 3:", score_3)
    print()


    # Тест 4: нет совпадений
    resume_4 = "Python pandas numpy"

    job_4 = "AutoCAD construction architecture"

    score_4 = calculate_match_score(resume_4, job_4, debug=True)

    print("Match score 4:", score_4)

