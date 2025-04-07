from App.models import Ingredient, Recipe
from App.database import db

def add_recipe(id, name, description, image, yt, category_name):
    recipe = Recipe(id=id, name=name, description=description, image=image, yt=yt, category_name=category_name)
    db.session.add(recipe)
    db.session.commit()
    return recipe

def add_recipe_ingredient(recipe_id, ingredient_name):
    ingredient = Ingredient.query.filter_by(name=ingredient_name).first()
    recipe = Recipe.query.filter_by(id=recipe_id).first()

    if not ingredient:
        return False

    if recipe.ingredient == None or ingredient not in recipe.ingredient:
        recipe.ingredient.append(ingredient)
        db.session.add(recipe)
        db.session.commit()
    return True

def get_recipe(name):
    recipe = Recipe.query.filter_by(name=name).first()
    if recipe:
        return recipe
    return None

def get_category_recipes(name):
    recipes = Recipe.query.filter_by(category_name=name).all()

    if recipes:
        return recipes
    return None

def get_all_recipes():
    recipes = Recipe.query.all()
    if recipes:
        return recipes
    return None