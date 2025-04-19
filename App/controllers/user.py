from App.models import User, Ingredient, Recipe
from App.database import db

def create_user(username, email, password):
    newuser = User(username=username, email=email, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def add_user_ingredient(id, ingredient_name):
    user = get_user(id)
    if not user:
        return None
    ingredient = Ingredient.query.filter_by(name=ingredient_name).first()
    if not ingredient:
        return None
    if ingredient not in user.ingredient:
        user.ingredient.append(ingredient)
        db.session.add(user)
        db.session.commit()
    return True

def remove_user_ingredient(id, ingredient_name):
    user = get_user(id)
    if not user:
        return None
    ingredient = Ingredient.query.filter_by(name=ingredient_name).first()
    if not ingredient:
        return None
    if ingredient in user.ingredient:
        user.ingredient.remove(ingredient)
        db.session.add(user)
        db.session.commit()
    return True

def add_user_recipe(id, recipe_id):
    user = get_user(id)
    if not user:
        return None
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if not recipe:
        return None
    if recipe not in user.recipe:
        user.recipe.append(recipe)
        db.session.add(user)
        db.session.commit()
    return True

def remove_user_recipe(id, recipe_id):
    user = get_user(id)
    if not user:
        return None
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if not recipe:
        return None
    if recipe in user.recipe:
        user.recipe.remove(recipe)
        db.session.add(user)
        db.session.commit()
    return True