from .user import create_user
from .recipe import add_ingredient, add_category, add_recipe,  add_recipe_ingredient
from App.database import db
import json
from urllib.request import urlopen

def initialize():
    db.drop_all()
    db.create_all()

    #code from https://stackabuse.com/how-to-get-json-from-a-url-in-python
    ingredients_url = urlopen('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
    category_url = urlopen('https://www.themealdb.com/api/json/v1/1/categories.php')
    
    if ingredients_url.getcode() == 200:
        data = json.loads(ingredients_url.read().decode('utf-8'))
        ingredients = data['meals']
        for ingredient in ingredients:
            add_ingredient(ingredient['idIngredient'], ingredient['strIngredient'], ingredient['strDescription'])
    else:
        print('Error Loading Database Ingredients')
    
    if category_url.getcode() == 200:
        data = json.loads(category_url.read().decode('utf-8'))
        categories = data['categories']

        for category in categories:
            new_cat = add_category(category['idCategory'], category['strCategory'], category['strCategoryDescription'], category['strCategoryThumb'])
            
            if new_cat:
                cat = category['strCategory'] 
                recipes_url = urlopen(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={cat}')

                if recipes_url.getcode() == 200:
                    recipe_data = json.loads(recipes_url.read().decode('utf-8'))
                    recipes = recipe_data['meals']

                    for id in recipes:
                        recipe_details_url = urlopen(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id['idMeal']}')

                        if(recipe_details_url.getcode() == 200):
                            recipe_details_data = json.loads(recipe_details_url.read().decode('utf-8'))
                            recipe_details = recipe_details_data['meals']

                            for recipe_detail in recipe_details:
                                add_recipe(recipe_detail['idMeal'], recipe_detail['strMeal'], recipe_detail['strInstructions'], recipe_detail['strMealThumb'], recipe_detail['strYoutube'], category['strCategory'])

                                string = "strIngredient"
                                i = 1
                                # add_recipe_ingredient(recipe_detail['idMeal'], recipe_detail[f'{string + str(i)}'])

                                while i <= 20 and recipe_detail[f'{string + str(i)}'] is not "":
                                    add_recipe_ingredient(recipe_detail['idMeal'], recipe_detail[f'{string + str(i)}'])
                                    i = i + 1
                                    
                        else:
                            print('Error Loading Database Recipes Details')
                else:
                    print('Error Loading Database Recipes')

    else:
        print('Error Loading Database Categories') 

    create_user('bob', 'bobpass')
