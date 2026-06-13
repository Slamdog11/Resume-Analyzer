from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume, jd):

    documents = [resume, jd]

    cv = CountVectorizer()

    matrix = cv.fit_transform(documents)

    similarity = cosine_similarity(matrix)

    score = similarity[0][1] * 100

    return round(score, 2)