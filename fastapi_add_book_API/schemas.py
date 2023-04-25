from pydantic import BaseModel

class Address_Validation(BaseModel):
   
    """
        Validation schema using pydantic 
    """

    id : int
    name : str
    email : str
    phone : str
    address_1 : str
    address_2 : str
    zip_code : str
    latitude : str
    longitude : str
    city : str
    country : str