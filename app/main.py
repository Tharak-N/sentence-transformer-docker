
from fastapi import FastAPI

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

app = FastAPI()

@app.get("")
async def root():
  return "Hola!"

@app.get("/st_docker")
async def sentence_transformer_docker():
  embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
  embeddings = embed_model.get_text_embedding("Hello world!")
  print(len(embeddings))
  pass