from App.database import db

class UserRecipe(db.Model):
    __tablename__ = 'user_recipe'
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id =  db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
