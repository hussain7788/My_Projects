
from fastapi import FastAPI, Depends
from sqlalchemy import and_, or_

app = FastAPI()
import models , schemas
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import logging

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get('/')
def get_all_addresses(db: Session = Depends(get_session), latitude:str=None, longitude:str=None):

    """
        Fetch all addresses from database 
        fetch data based on latitude and longitude query params
    """
    logging.info(f'Executing {get_all_addresses.__name__} function. \
                 Fetching all addresses' )
    if latitude and longitude:
        logging.info(f"Fetching latitude: {latitude} and longitude: {longitude}")
        data = db.query(models.Address).filter(and_(models.Address.latitude==latitude, models.Address.longitude==longitude)).all()
        logging.info(f"Successfully fetched latitude and longitude..")
    else:
        data = db.query(models.Address).all()

    logging.info(f"Successfully fetched all addresses..")
    return data


@app.post('/')
def add_address(addr: schemas.Address_Validation, db: Session = Depends(get_session)):

    """
        Add address in database with proper validations
    """
    logging.info(f'Executing {add_address.__name__} function. \
                 Validating and Adding address data' )
    data = models.Address(id=addr.id, name=addr.name, email=addr.email, phone=addr.phone, 
                          address_1=addr.address_1, address_2=addr.address_2,
                          zip_code=addr.zip_code, latitude=addr.latitude,
                          longitude=addr.longitude, city=addr.city, 
                          country=addr.country)
    db.add(data)
    db.commit()
    db.refresh(data)
    logging.info(f"Successfully added address data")
    return data

@app.get('/{id}')
def get_address(id: int, db: Session = Depends(get_session)):
    
    """
        Fetch address based on ID from the database
    """
    logging.info(f'Executing {get_address.__name__} function.\
                  Getting address by ID: {id}' )
    data = db.query(models.Address).get(id)
    logging.info(f"Successfully fetched address by ID: {id}")
    return data

@app.put('/{id}')
def update_address(id: int, addr: schemas.Address_Validation, db: Session = Depends(get_session)):
    
    """
        Update address by ID with proper validations
    """
    logging.info(f'Executing {update_address.__name__} function.\
                  Updating validated address by ID: {id}')
    data = db.query(models.Address).get(id)
    data.name=addr.name
    data.email=addr.email
    data.phone=addr.phone
    data.address_1=addr.address_1
    data.address_2=addr.address_2
    data.zip_code=addr.zip_code
    data.latitude=addr.latitude
    data.longitude=addr.longitude
    data.city=addr.city
    data.country=addr.country
    db.commit()
    logging.info(f"Successfully updated address by ID: {id}")
    return data

@app.delete('/')
def delete_address(id: int, db: Session = Depends(get_session)):
    
    """
        Delete address from database by given ID
    """

    logging.info(f'Executing {delete_address.__name__} function.\
                  Deleting address by ID: {id}')
    data = db.query(models.Address).get(id)
    db.delete(data)
    db.commit()
    db.close()
    logging.info(f"Successfully deleted address by ID: {id}")
    return "Address was deleted.."

