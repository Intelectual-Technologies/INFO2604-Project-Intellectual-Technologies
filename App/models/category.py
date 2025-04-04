from App.database import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(20), nullable=False, unique=True)
    description =  db.Column(db.String(300), nullable=False, unique=True)
    image = db.Column(db.String(50), nullable=False)

    def __init__(self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image