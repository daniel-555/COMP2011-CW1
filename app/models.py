from app import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    module = db.Column(db.String(10), nullable=False)
    deadline = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean)