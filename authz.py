import os
from oso_cloud import Oso, Value
from dotenv import load_dotenv
from models import Role, User, UserAssignment
from sqlalchemy.orm import Session

load_dotenv()

def setup_oso(db: Session):
    oso = Oso(url=os.getenv("OSO_URL"), api_key=os.getenv("OSO_API_KEY"), data_bindings="./app/authorization/facts.yaml")
    users = db.query(User).all()
    roles = db.query(Role).all()
    assignments = db.query(UserAssignment).all()
    

    for user in users:
        user_assignment = [a for a in assignments if a.user_id == user.id][0]
        role = [r for r in roles if r.id == user_assignment.role_id][0]
        user_fact = Value(type="User", id=user.id)
        department_fact = Value(type="Department", id=user_assignment.department_id)
        oso.insert(("has_role", user_fact, role.role_name.value, department_fact))

    return oso
