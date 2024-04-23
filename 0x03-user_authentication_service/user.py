#!/usr/bin/env python3
"""
User model module
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class representing the users table
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email: str, hashed_password: str,
                 session_id: str = None, reset_token: str = None):
        """
        Inititalise a new User instance
        """
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

    def __repr__(self) -> str:
        """
        Return a string representation of the User instance
        """
        return " < User(id={}, email='{}', session_id='{}',
                        reset_token='{}') > ".format(
                self.id, self.email, self.session_id, self.reset_token
                )

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the User instance
        """
        return {
                'id': self.id,
                'email': self.email,
                'session_id': self.session_id,
                'reset_token': self.reset_token
                }
