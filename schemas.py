from pydantic import BaseModel


class Cat(BaseModel):
    id :int
    name: str
    age : str
    colour : str
    description : str
    location : str #secret

class CatResponse(BaseModel):
    id : int
    name:str
    age : str
    colour : str

    class config:
        from_attribute=True