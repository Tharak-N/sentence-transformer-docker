
from fastapi import FastAPI


app = FastAPI()

@app.get("")
async def root():
  return "Hola!"

@app.get("/st_docker")
async def sentence_transformer_docker():
  pass