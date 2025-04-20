from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user 

from.index import index_views

from App.controllers import (
    get_category_recipes,
    get_category,
    get_recipe,
    get_all_recipes,
    jwt_required
)

recipe_views = Blueprint('recipe_views', __name__, template_folder='../templates')

@recipe_views.route('/render-recipes/<string:name>', methods=['GET'])
def get_recipe_page(name):
    category = get_category(name)
    if category:
        recipes = get_category_recipes(category.name)
        if recipes:
            return render_template('recipes.html', recipes=recipes, category_name = category.name)
            
        else:
            print("Category does not contain recipes")
            return jsonify({'message': f'{category.name} does not contain recipes'})
    else:
        print("Category does not exist")
    return redirect(url_for('user_views.get_categories_page'))


@recipe_views.route('/render-details/<string:name>', methods=['GET'])
def get_details_page(name):
    category = get_category(name)
    if category:
        return render_template('details.html', item_details=category)
    else:
        recipe = get_recipe(name)
        if recipe:
            return render_template('details.html', item_details=recipe)
    return redirect(url_for('user_views.get_categories_page'))


@recipe_views.route('/render-all-recipes', methods=['GET'])
def get_all_recipes_page():
    recipes = get_all_recipes()
    if recipes:
        return render_template('recipes.html', recipes=recipes)
    return redirect(url_for('user_views.get_categories_page'))

@recipe_views.route('/search-recipes', methods=['POST'])
def search_recipes():
    search_query = request.form.get('search')
    if search_query:
        recipes = get_all_recipes()
        filtered_recipes = [recipe for recipe in recipes if search_query.lower() in recipe.name.lower()]
        return render_template('recipes.html', recipes=filtered_recipes)
    return redirect(request.referrer)