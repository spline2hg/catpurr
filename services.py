from models import CatProfile
from schemas import Cat,CatResponse
from sqlalchemy.orm import Session

def create_cat(catprofile:Cat , db:Session):
    cat = CatProfile(**catprofile.model_dump())
    db.add(cat)
    db.commit()
    db.refresh(cat)

    return cat

def all_cats(db:Session):
    cats = db.query(CatProfile).all()
    return cats