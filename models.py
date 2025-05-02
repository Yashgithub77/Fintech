from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50))
    source = db.Column(db.String(100))
    amount = db.Column(db.Float)
    timestamp = db.Column(db.String(50))
