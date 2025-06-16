from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(100))
    member = db.Column(db.String(100))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    item_name = db.Column(db.String(200))
    option = db.Column(db.String(100))
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f"<Order {self.member} - {self.item_name} ({self.quantity})>"
