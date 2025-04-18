from App.database import db

class UserIngredient(db.Model):
    __tablename__ = 'user_ingredient'
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ingredient_id =  db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
