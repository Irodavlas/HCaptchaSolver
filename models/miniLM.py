import torch 
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
class NewMiniLM:
    def __init__(self, model="all-MiniLM-L6-v2"):
        print(f"loading model {model}")
        self.model = SentenceTransformer(model) 

    def encode_embedding(self, label : str): 
        return self.model.encode(label)
    
    def cosine_similarity(self, prompt_embedding, label_embedding):
        return cosine_similarity([prompt_embedding], [label_embedding])[0][0]