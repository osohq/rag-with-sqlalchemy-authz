from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, func, Enum
from sqlalchemy.orm import relationship, declarative_base
from pgvector.sqlalchemy import Vector
import enum

# Models
Base = declarative_base()

class RoleType(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    MEMBER = "member"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    documents = relationship("Document", back_populates="creator")
    assignments = relationship("UserAssignment", back_populates="user")


class Department(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    documents = relationship("Document", back_populates="department")
    assignments = relationship("UserAssignment", back_populates="department")


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(Enum(RoleType), nullable=False, unique=True)
    assignments = relationship("UserAssignment", back_populates="role")


class UserAssignment(Base):
    __tablename__ = 'user_assignments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='RESTRICT'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id', ondelete='CASCADE'), nullable=False)
    user = relationship("User", back_populates="assignments")
    role = relationship("Role", back_populates="assignments")
    department = relationship("Department", back_populates="assignments")

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    content_embeddings = Column(Vector(1536)) 
    created_by = Column(Integer, ForeignKey('users.id', ondelete='RESTRICT'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id', ondelete='RESTRICT'), nullable=False)
    creator = relationship("User", back_populates="documents")
    department = relationship("Department", back_populates="documents")