from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import secrets
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    tokens = relationship("RememberToken", back_populates="user")
    avatar_url = Column(String, nullable=True)


class RememberToken(Base):
    __tablename__ = 'remember_tokens'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token = Column(String(255), unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="tokens")

    @staticmethod
    def generate_token():
        return secrets.token_urlsafe(32)

