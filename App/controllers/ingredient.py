from App.models import Ingredient
from App.database import db

def add_ingredient(id, name, description):
    ingredient = Ingredient(id=id, name=name, description=description)
    db.session.add(ingredient)
    db.session.commit()
    return ingredient

def get_all_ingredients():
    ingredients = Ingredient.query.all()
    if ingredients:
        return ingredients
    return None
