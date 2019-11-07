from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Product(Base):
   __tablename__ = 'students'
   id = Column(Integer, primary_key=True)
   price = Column(Integer)
   picture link= Column(String)
   description = Column(String)

