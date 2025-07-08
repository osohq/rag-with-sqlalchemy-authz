from models import RoleType


user_data = [
    {"name": "pam"},
    {"name": "michael"},
    {"name": "dwight"}
]

department_data = [
    {"name": "Engineering"},
    {"name": "Human Resources"}
]

role_data = [
    {"role_name": RoleType.ADMIN},
    {"role_name": RoleType.MANAGER},
    {"role_name": RoleType.MEMBER}
]

document_data = [
    {"title": "document_1", "content": "Michael said that Dwight is a labrador retriever", "created_by": 1, "department_id": 1},
    {"title": "document_2", "content": "Dwight said that Pam likes strawberry milkshakes", "created_by": 2, "department_id": 2},
    {"title": "document_3", "content": "Pam said that Michael hates strawberry milkshakes", "created_by": 3, "department_id": 2}
]

user_assignment_data = [
    {"user_id": 1, "role_id": 1, "department_id": 1},
    {"user_id": 2, "role_id": 2, "department_id": 2},
    {"user_id": 3, "role_id": 3, "department_id": 2}
]