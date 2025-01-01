from fastapi import FastAPI, Depends
from models import CatProfile
from schemas import Cat
from db import get_db
from sqlalchemy.orm import Session
import services
from db import  Base,engine

cat = FastAPI()
 
Base.metadata.create_all(bind=engine) 
print("created tables")


@cat.get("/")
def home_cat():
    return {"slogan":"Welcome to Purrtopia, where every meow tells a story!"}


@cat.post("/purrentry")
def create_cat_profile(cat_i:Cat , db:Session = Depends(get_db),):
    return services.create_cat(cat_i,db)


@cat.get("/purrview")
def get_all_cats(db:Session=Depends(get_db)):
    return services.all_cats(db)