
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from ai import generate_embeddings
from models import Base, User, Department, Role, UserAssignment, Document
from data import user_data, department_data, role_data, document_data, user_assignment_data

def enable_pgvector_on_neon(session: Session):
    session.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
    session.commit()

def setup_db(db_url: str):
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    with SessionLocal() as session:
        session.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        session.commit()

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:
        for user in user_data:
            session.add(User(name=user["name"]))
        for department in department_data:
            session.add(Department(name=department["name"]))
        for role in role_data:
            session.add(Role(role_name=role["role_name"]))
        for document in document_data:
            session.add(Document(title=document["title"], content=document["content"], created_by=document["created_by"], department_id=document["department_id"]))
        for user_assignment in user_assignment_data:
            session.add(UserAssignment(user_id=user_assignment["user_id"], role_id=user_assignment["role_id"], department_id=user_assignment["department_id"]))

        documents = session.query(Document).all()
        for document in documents:
            document.content_embeddings = generate_embeddings(document.content)
            session.add(document)
        session.commit()

    return SessionLocal()

def cleanup_db(db_url: str):
    engine = create_engine(db_url)
    Base.metadata.drop_all(bind=engine)
    print("All model tables dropped successfully!")