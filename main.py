
from dotenv import load_dotenv
import os
from openai import OpenAI
from authz import setup_oso
from chatbot import DemoChatbot
from db import cleanup_db, setup_db

load_dotenv()

def run_demo():
    db_url = os.getenv("DATABASE_URL")
    cleanup_db(db_url=db_url)

    db = setup_db(db_url=db_url)
    oso = setup_oso(db)

    chatbot = DemoChatbot(db, oso)
    chatbot.run()

if __name__ == "__main__":
    run_demo()