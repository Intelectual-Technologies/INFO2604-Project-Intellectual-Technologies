from App.models import Category
from App.database import db

def add_category(id, name, description, image):
    category = Category(id=id, name=name, description=description, image=image)
    db.session.add(category)
    db.session.commit()
    return category

def get_category(name):
    category = Category.query.filter_by(name=name).first()
    if category:
        return category
    else:
        return None

def get_all_categories():
    categories = Category.query.all()
    if categories:
        return categories
    else:
        return None