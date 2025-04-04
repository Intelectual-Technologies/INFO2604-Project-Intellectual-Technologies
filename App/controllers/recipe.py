from App.models import Ingredient, Category, Recipe
from App.database import db

def add_ingredient(id, name, description):
    ingredient = Ingredient(id=id, name=name, description=description)
    db.session.add(ingredient)
    db.session.commit()
    return ingredient

def add_category(id, name, description, image):
    category = Category(id=id, name=name, description=description, image=image)
    db.session.add(category)
    db.session.commit()
    return category

def get_category(id):
    category = Category.query.filter_by(id=id).first()
    if category:
        return category
    else:
        return False

def get_all_categories():
    categories = Category.query.all()
    if categories:
        return categories
    else:
        return False

def add_recipe(id, name, instructions, image, yt, category_name):
    recipe = Recipe(id=id, name=name, instructions=instructions, image=image, yt=yt, category_name=category_name)
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