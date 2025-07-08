from pgvector import Vector
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_embeddings(content: str):
    embedding = openai_client.embeddings.create(input=content, model="text-embedding-3-large")
    return Vector(embedding.data[0].embedding)

def generate_response(prompt: str, documents: str):
    system_prompt = f"""
        You are a helpful assistant that can answer questions about the following documents in the database:
        only answer questions that are related to the documents.
        {documents}
        """

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
        )
    return response.choices[0].message.content

