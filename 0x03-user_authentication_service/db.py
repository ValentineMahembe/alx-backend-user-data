"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:

    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.create_all(self._engine)
        self._session_maker = sessionmaker(bind=self._engine)

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database
        """
        new_user = User(email=email, hashed_password=hashed_password)
        with self._session_maker() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        return new_user
