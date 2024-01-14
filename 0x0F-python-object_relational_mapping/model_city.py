#!/usr/bin/python3
"""
City model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """City class that represents cities SQL table

    Args:
        Base (declarative): declare table representer object.
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        """string representation of State class
        Returns:
            str: representation of State class.
        """
        return f"{self.id}: ({self.name}) {self.state_id}"
