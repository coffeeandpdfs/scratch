from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, validators, DateField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AmortizationForm(FlaskForm):
    loan_amount = IntegerField('Loan Amount:', [validators.required()])
    annual_interest_rate = DecimalField('Interest Rate: (Format: 0.04125)', [validators.required()], places=5)
    years = IntegerField('Years:', [validators.required()])
    payment_amount = IntegerField("Payment (optional)")
    additional_amount = IntegerField('Additional Payment:', [validators.optional()])
    start_date = DateField('Start Date: (Format: mm-dd-yyyy)', format='%m-%d-%Y')
    submit = SubmitField('Submit')


class BudgetForm(FlaskForm):
    lineitem = StringField('Item Name: ')
    amount = DecimalField('Amount: ')
    flexible = StringField('Flexible: ')
    notes = StringField('Additional Notes: ')
    submit = SubmitField('Submit')
