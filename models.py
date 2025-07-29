from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Form(db.Model):
    __tablename__ = 'form'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Form {}".format(self.id)

