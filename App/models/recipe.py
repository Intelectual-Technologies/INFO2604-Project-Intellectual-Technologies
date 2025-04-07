from App.database import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(20), nullable=False, unique=True)
    description =  db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(50), nullable=False)
    yt = db.Column(db.String(30), nullable=False)
    ingredient = db.relationship('Ingredient', secondary= 'recipe_ingredient', backref=db.backref('recipe', lazy = True))
    category_name =  db.Column(db.String(20), db.ForeignKey('category.name'), nullable=False)

    def __init__(self, id, name, description, image, yt, category_name):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.yt = yt
        self.category_name = category_name