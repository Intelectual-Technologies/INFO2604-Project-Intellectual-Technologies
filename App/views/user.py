from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user 

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    add_user_ingredient,
    remove_user_ingredient,
    get_all_ingredients,
    add_user_recipe,
    remove_user_recipe,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
@jwt_required()
def get_user_page():
    ingredeients = get_all_ingredients()
    return render_template('users.html', ingredients=ingredeients)

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['email'], data['password'])
    return redirect(url_for('auth_views.get_login_page'))

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    email = data['username'] + "@mail.com"
    user = create_user(data['username'], email, data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})

@user_views.route('/add-user-ingredient/<string:name>', methods=['GET'])
@jwt_required()
def add_user_ingredient_action(name):
    ingredient = add_user_ingredient(current_user.id, name)
    
    if not ingredient:
        flash("Ingredient not found")
        return redirect(url_for('user_views.get_user_page'))
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/remove-user-ingredient/<string:name>', methods=['GET'])
@jwt_required()
def remove_user_ingredient_action(name):
    ingredient = remove_user_ingredient(current_user.id, name)
    
    if not ingredient:
        flash("Ingredient not found")
        return redirect(url_for('user_views.get_user_page'))
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/add-user-recipe/<int:id>', methods=['POST'])
@jwt_required()
def add_user_recipe_action(id):
    recipe = add_user_recipe(current_user.id, id)
    
    if not recipe:
        return jsonify({'success': False, 'message': 'Recipe not found'}), 404
    return jsonify({'success': True, 'message': 'Recipe added to favorites'}), 200

@user_views.route('/remove-user-recipe/<int:id>', methods=['POST'])
@jwt_required()
def remove_user_recipe_action(id):
    recipe = remove_user_recipe(current_user.id, id)
    
    if not recipe:
        return jsonify({'success': False, 'message': 'Recipe not found'}), 404
    return jsonify({'success': True, 'message': 'Recipe removed from favorites'}), 200
