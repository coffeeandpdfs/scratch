from flask import render_template, session, redirect, url_for
from datetime import date, datetime
from . import main
from .forms import AmortizationForm
import pandas as pd
import numpy as np
from ..functions.functions import amortize


@main.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@main.route('/amortization', methods=['GET', 'POST'])
def amortization_page():
    # Web form to for an amortization calculator
    form = AmortizationForm()
    if form.validate_on_submit():
        loan_amount = form.loan_amount.data
        interest_rate = form.annual_interest_rate.data
        years = form.years.data
        #PaymentsPerYear = form.payments_per_year.data
        payment = form.payment_amount.data
        additional_payment = form.additional_amount.data
        if form.start_date.data:
            start_date = form.start_date.data
        else:
            start_date = date.today()

        a = amortize(loan_amount, interest_rate, years, start_date, payment=payment, 
                        additional_payment=additional_payment)
        df = pd.DataFrame(a).set_index('Period').sort_index(ascending=False)

        return render_template('amortization_model.html', form=form, data=df.to_html())
    return render_template('amortization_model.html', form=form)


@main.route('/blog', methods=['GET', 'POST'])
def blog_posts():
    # Placeholder for blog
    pass

@main.route('/budget/', methods=['GET', 'POST'])
def current_budget():
    # Displays the current budget
    # Options to update dollar amounts
    # Item1 | $Total | [Modification]
    # Item2 | $Total | [Modification]
    #                 Submit
    # return render_template('budget.html')
    pass


@main.route('/updatebudget', methods=['GET','POST'])
def update_budget():
    # Displays calculator to post new costs to the budget
    # Item1 | $Total | Remaining | [Modification]
    # Item2 | $Total | Remaining | [Modification]
    #                              Submit
    # return render_template('updatebudget.html')
    pass


@main.route('/budgetchanges', methods=['GET','POST'])
def budget_changes():
    # Display the previous changes to the budget
    # Display the debits associated with the budget
    # return render_template('budgetchanges.html')
    pass
