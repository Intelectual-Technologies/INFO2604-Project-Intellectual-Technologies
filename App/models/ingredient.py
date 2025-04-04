from App.database import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(20), nullable=False, unique=True)
    description =  db.Column(db.String(300), nullable=True)

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description= description

