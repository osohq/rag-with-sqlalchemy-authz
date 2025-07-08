import os
from oso_cloud import Value
from dotenv import load_dotenv
from models import Role, User, UserAssignment
from sqlalchemy_oso_cloud import get_oso
from sqlalchemy.orm import Session

load_dotenv()

def setup_oso(db: Session):
    oso = get_oso()
    assignments = db.query(UserAssignment).all()
    roles = db.query(Role).all()
    
    for assignment in assignments:
        user_fact = Value(type="User", id=assignment.user_id)
        department_fact = Value(type="Department", id=assignment.department_id)
        role = [r for r in roles if r.id == assignment.role_id][0]
        oso.insert(("has_role", user_fact, role.role_name.value, department_fact))

    return oso
