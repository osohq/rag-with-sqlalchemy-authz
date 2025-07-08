from oso_cloud import Oso, Value
from sqlalchemy import text
from sqlalchemy.orm import Session
from openai import OpenAI

from ai import generate_embeddings, generate_response
from models import User

user_options = [
    {
        "name": "pam",
        "department": "human resources",
        "role": "member"
    },
    {
        "name": "michael",
        "department": "engineering",
        "role": "manager"
    },
    {
        "name": "dwight",
        "department": "engineering",
        "role": "member"
    }
]


class DemoChatbot:
    def __init__(self, db: Session, oso: Oso, user: User = None):
        self.db = db
        self.oso = oso
        self.user = user

    def handle_response(self, prompt: str):
        # Where new library comes in
        prompt_embeddings = generate_embeddings(prompt)
        user_fact = Value(type="User", id=self.user.id)
        query = self.oso.list_local(user_fact, "read", "Document", "content")
        result = self.db.execute(text(query), {"user_id": self.user.id})

        documents = result.fetchall()
        documents_str = "\n".join([document[0] for document in documents])
        response = generate_response(f"{documents_str}\n\n{prompt}")
        return response
    
    def _set_user(self, user_name: str):
        user = self.db.query(User).filter(User.name == user_name).first()
        self.user = user
    
    def _print_user_options(self):
        print("Available users:")
        for user in user_options:
            print(f"- {user['name']}")
    
    def run(self):
        self._print_user_options()
        user_name = input("Enter a user name: ")
        self._set_user(user_name)
        while True:
            prompt = input("Enter a prompt: ")
            response = self.handle_response(prompt)
            print(response)

    # add click frontend
