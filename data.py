from models import RoleType


user_data = [
    {"name": "jane"},
    {"name": "jerry"},
    {"name": "george"},
    {"name": "karen"}
]

department_data = [
    {"name": "Engineering"},
    {"name": "Human Resources"}
]

role_data = [
    {"role_name": RoleType.MANAGER},
    {"role_name": RoleType.MEMBER}
]

user_assignment_data = [
    {"user_id": 1, "role_id": 1, "department_id": 1}, # Jane is a manager in Engineering
    {"user_id": 2, "role_id": 2, "department_id": 1}, # Jerry is a member in Engineering
    {"user_id": 3, "role_id": 1, "department_id": 2}, # George is a manager in HR
    {"user_id": 4, "role_id": 2, "department_id": 2} # Karen is a member in HR
]

document_data = [
    {"title": "document_1", "content": "Jane thinks Jerry is a good programmer", "created_by": 1, "department_id": 1},
    {"title": "document_2", "content": "Jerry is working on a new project, codenamed 'The Great Escape'", "created_by": 2, "department_id": 1},
    {"title": "document_3", "content": "Jerry and Karen are dating", "created_by": 3, "department_id": 2},
    {"title": "document_4", "content": "George's birthday is on July 10th", "created_by": 1, "department_id": 2, "is_public": True},
    {"title": "document_5", "content": "Karen is 49 years old", "created_by": 4, "department_id": 2}
]

# A manager can read a document if it is in their department
# A member can read a document if they are the creator
# Anyone can read a public document

# Jane can read document 1, 2 and 4
# Jerry can read document 2 and 4
# George can read document 3, 4, and 5
# Karen can read document 4 and 5

# Test prompts:

test_prompts = {
    "jane": [
        "What does Jane think about Jerry's programming skills?", # Should know
        "What project is Jerry working on?", # Should know
        "Are Jerry and Karen dating?", # Should NOT know
        "When is George's birthday?", # Should know
        "How old is Karen?", # Should NOT know
    ],
    "jerry": [
        "What does Jane think about Jerry's programming skills?", # Should NOT know
        "What project is Jerry working on?", # Should know
        "Are Jerry and Karen dating?", # Should NOT know
        "When is George's birthday?", # Should know
        "How old is Karen?", # Should NOT know
    ],
    "george": [
        "What does Jane think about Jerry's programming skills?", # Should NOT know
        "What project is Jerry working on?", # Should NOT know
        "Are Jerry and Karen dating?", # Should know
        "When is George's birthday?", # Should know
        "How old is Karen?", # Should know
    ],
    "karen": [
        "What does Jane think about Jerry's programming skills?", # Should NOT know
        "What project is Jerry working on?", # Should NOT know
        "Is Karen dating Jerry?", # Should NOT know
        "When is George's birthday?", # Should know
        "How old is Karen?", # Should know
    ]
}

