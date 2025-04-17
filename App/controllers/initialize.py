from .user import create_user
from .category import add_category
from .ingredient import add_ingredient
from .recipe import add_recipe,  add_recipe_ingredient
from App.database import db
import json
from urllib.request import urlopen

def initialize():
    db.drop_all()
    db.create_all()
    
    with open('ingredients.json') as file_I:
        data = json.load(file_I)
        ingredients = data['meals']

    for ingredient in ingredients:
        add_ingredient(ingredient['idIngredient'], ingredient['strIngredient'], ingredient['strDescription'])
    

    with open('categories.json') as file_C:
        data = json.load(file_C)
        categories = data['categories']

    for category in categories:
        add_category(category['idCategory'], category['strCategory'], category['strCategoryDescription'], category['strCategoryThumb'])

    with open('recipes.json') as file_R:
        recipe_details_data = json.load(file_R)
        recipe_details = recipe_details_data['meals']
         
    for recipe_detail in recipe_details:
        add_recipe(recipe_detail['idMeal'], recipe_detail['strMeal'], recipe_detail['strInstructions'], recipe_detail['strMealThumb'], recipe_detail['strYoutube'], recipe_detail['strCategory'])
        string = "strIngredient"
        i = 1

        while i <= 20 and recipe_detail[f'{string + str(i)}'] != "":
            add_recipe_ingredient(recipe_detail['idMeal'], recipe_detail[f'{string + str(i)}'])
            i = i + 1
                    
    create_user('bob', 'bob@mail.com', 'bobpass')
