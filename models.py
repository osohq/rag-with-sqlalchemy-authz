from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import Mapped, declarative_base
import sqlalchemy_oso_cloud.orm as oso
from pgvector.sqlalchemy import Vector
import enum

# Models
Base = declarative_base()

class RoleType(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    MEMBER = "member"

class User(Base, oso.Resource):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    documents = oso.relation("Document", back_populates="creator")
    assignments = oso.relation("UserAssignment", back_populates="user")


class Department(Base, oso.Resource):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    documents = oso.relation("Document", back_populates="department")
    assignments = oso.relation("UserAssignment", back_populates="department")


class Role(Base, oso.Resource):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(Enum(RoleType), nullable=False, unique=True)
    assignments = oso.relation("UserAssignment", back_populates="role")


class UserAssignment(Base, oso.Resource):
    __tablename__ = 'user_assignments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='RESTRICT'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id', ondelete='CASCADE'), nullable=False)
    user = oso.relation("User", back_populates="assignments")
    role = oso.relation("Role", back_populates="assignments")
    department = oso.relation("Department", back_populates="assignments")

class Document(Base, oso.Resource):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    content_embeddings = Column(Vector(3072)) 
    created_by = Column(Integer, ForeignKey('users.id', ondelete='RESTRICT'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id', ondelete='RESTRICT'), nullable=False)
    creator = oso.relation("User", back_populates="documents")
    department = oso.relation("Department", back_populates="documents")
    is_public: Mapped[bool] = oso.attribute(default=False)