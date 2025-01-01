from sqlalchemy import Column,Integer,String
from db import Base


class CatProfile(Base):
    __tablename__="catprofile"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    age = Column(Integer)
    colour = Column(String)
    description = Column(String)
    location = Column(String)

