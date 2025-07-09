from oso_cloud import Oso, Value
from sqlalchemy import text
from sqlalchemy.orm import Session

from ai import generate_embeddings, generate_response
from db import get_authorized_documents
from models import User

class DemoChatbot:
    def __init__(self, db: Session, oso: Oso):
        self.db = db
        self.oso = oso
        self.user = None
        self.users = self._get_users()

    def handle_response(self, prompt: str):
        prompt_embeddings = generate_embeddings(prompt)
        documents = get_authorized_documents(self.db, self.user, "read", prompt_embeddings)
        documents_str = "\n".join([document.title + "\n" + document.content for document in documents])
        response = generate_response(prompt, documents_str)
        return response
    
    def _get_users(self):
        return self.db.query(User).all()
    
    def _set_user(self, user_name: str):
        user = [u for u in self.users if u.name == user_name][0]
        self.user = Value(type="User", id=user.id)
    
    def _print_user_options(self):
        print("Available users:")
        for user in self.users:
            print(f"- {user.name} - {user.assignments[0].role.role_name} - {user.assignments[0].department.name}")
    
    def run(self):
        self._print_user_options()
        user_name = input("Enter a user name: ").lower()
        if user_name == "exit":
            return
        if user_name not in [u.name for u in self.users]:
            print("Invalid user name")
            return self.run()
        self._set_user(user_name)
        while True:
            prompt = input("Enter a prompt: ")
            if (prompt == "set_user"):
                self._print_user_options()
                user_name = input("Enter a user name: ")
                if user_name == "exit":
                    return
                if user_name not in [u.name for u in self.users]:
                    print("Invalid user name")
                self._set_user(user_name)
                continue
            response = self.handle_response(prompt)
            print(response)
