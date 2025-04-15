from fastapi import FastAPI, Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()

# Load the model ONCE into memory (fast startup)
model = SentenceTransformer('all-MiniLM-L6-v2', device="cuda")  # 384-dim, fast and solid

class EmbedRequest(BaseModel):
    text: str

@app.post("/embed")
async def embed(req: EmbedRequest):
    # Encode the text to get embedding
    embedding = model.encode(req.text, normalize_embeddings=True)
    return {"embedding": embedding.tolist()}
