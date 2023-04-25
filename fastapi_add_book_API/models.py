from sqlalchemy import Column, Integer, String
from database import Base

class Address(Base):
    
    """
        Creating model class and added required fields for address table
    """

    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(40))
    phone = Column(String(15))
    address_1 = Column(String(200))
    address_2 = Column(String(200))
    zip_code = Column(String(10))
    latitude = Column(String(50))
    longitude = Column(String(50))
    city = Column(String(50))
    country = Column(String(50))



