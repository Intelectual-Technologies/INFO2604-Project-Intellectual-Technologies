from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user 

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    get_all_categories,
    get_category,
    get_category_recipes,
    get_recipe,
    get_all_recipes,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    
    return render_template('users.html', users=users)

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['email'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/categories', methods=['GET'])
@jwt_required()
def get_categories_page():
    categories = get_all_categories()
    flash(f"Categories")
    return render_template('categories.html', categories=categories, category_detail=None)

@user_views.route('/render-details/<string:name>', methods=['GET'])
def get_details_page(name):
    category = get_category(name)
    if category:
        return render_template('details.html', item_details=category)
    else:
        recipe = get_recipe(name)
        if recipe:
            return render_template('details.html', item_details=recipe)
    return redirect(url_for('user_views.get_categories_page'))

@user_views.route('/back', methods=['GET'])
def back():
    return redirect(url_for(request.referrer))

@user_views.route('/render-recipes/<string:name>', methods=['GET'])
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

@user_views.route('/signup-page', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')

@user_views.route('/login-page', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@user_views.route('/render-all-recipes', methods=['GET'])
def get_all_recipes_page():
    recipes = get_all_recipes()
    if recipes:
        return render_template('recipes.html', recipes=recipes)
    return redirect(url_for('user_views.get_categories_page'))