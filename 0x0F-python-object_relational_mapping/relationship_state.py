#!/usr/bin/python3
"""
State model, bidirectional way with City model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """States class that represents states SQL table

    Args:
        Base (declarative): declare table representer object.
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True
                )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __repr__(self):
        """string representation of State class
        Returns:
            str: representation of State class.
        """
        return f"{self.id}: {self.name}"
