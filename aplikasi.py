pip install gensim
import streamlit as st
from gensim.models import KeyedVectors
import numpy as np

# Memuat model word2vec pra-latih (contoh menggunakan model Google News)
@st.cache(allow_output_mutation=True)
def load_model():
    model_path = 'GoogleNews-vectors-negative300.bin'  # Path ke model Word2Vec pra-latih
    model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    return model

# Fungsi untuk mendapatkan embedding sebuah kata
def get_word_embedding(word, model):
    try:
        embedding = model[word]
        return embedding
    except KeyError:
        st.error(f"'{word}' tidak ditemukan dalam model.")
        return None

# Fungsi untuk menghitung kesamaan kosinus antara dua vektor
def cosine_similarity(vec1, vec2):
    cos_sim = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    return cos_sim

st.title("Word Embeddings dengan Word2Vec")

# Memuat model
model = load_model()

# Input dari pengguna
word1 = st.text_input("Masukkan kata pertama:", value="king")
word2 = st.text_input("Masukkan kata kedua:", value="queen")

if word1 and word2:
    embedding1 = get_word_embedding(word1, model)
    embedding2 = get_word_embedding(word2, model)

    if embedding1 is not None and embedding2 is not None:
        similarity = cosine_similarity(embedding1, embedding2)
        st.write(f"Kesamaan kosinus antara '{word1}' dan '{word2}': {similarity:.4f}")

        # Menampilkan vektor embedding (opsional)
        st.write(f"Embedding untuk '{word1}':", embedding1)
        st.write(f"Embedding untuk '{word2}':", embedding2)
