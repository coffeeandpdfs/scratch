from . import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))


class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(db.Integer, primary_key=True)
    earner_name = db.Column(db.String(50))
    wage = db.Column(db.Float)
    hours = db.Column(db.Float)
    deductions = db.Column(db.Float)
    monthly_salary = db.Column(db.Float)
    yearly_salary = db.Column(db.Float)


class Budget(db.Model):
    __tablename__ = 'budget'
    id = db.Column(db.Integer, primary_key=True)
    lineitem = db.Column(db.String(100))
    amount = db.Column(db.Float)
    flexible = db.Column(db.String(25))
    notes = db.Column(db.String(100))
