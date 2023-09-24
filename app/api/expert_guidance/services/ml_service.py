import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')


def compute_expert_response(query: str, legal_dataset):
    # # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
    legal_dataset_vector = vectorizer.fit_transform(legal_dataset)

    print(query)
    # Vectorize query text
    query_vec = vectorizer.transform([query])

    # Calculate cosine similarity between query and legal documents
    similarities = cosine_similarity(legal_dataset_vector, query_vec).flatten()

    # Find the most relevant document
    most_relevant_index = similarities.argmax()

    return {"response": legal_dataset[most_relevant_index]}
