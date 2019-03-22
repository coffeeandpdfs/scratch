from flask import render_template, session, redirect, url_for, request
from datetime import date, datetime
from . import main
from .forms import AmortizationForm, BudgetForm, BudgetTable
import pandas as pd
import numpy as np
from ..functions.functions import amortize
from .. import db
from ..models import Budget


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


@main.route('/budget/', methods=['GET', 'POST'])
def current_budget():
    # Displays the current budget
    # Options to update dollar amounts
    # Item1 | $Total | [Modification]
    # Item2 | $Total | [Modification]
    #                 Submit
    # return render_template('budget.html')
    data = db.session.query(Budget).all()
    return render_template('budget_view.html', data=data)


@main.route('/updatebudget/<int:id>', methods=['GET','POST'])
def update_budget(id):
    # Displays calculator to post new costs to the budget
    # Item1 | $Total | Remaining | [Modification]
    # Item2 | $Total | Remaining | [Modification]
    #                              Submit
    # return render_template('updatebudget.html')
    budget_item = db.session.query(Budget).filter(Budget.id == id).first()
    if budget_item:
        form = BudgetForm(formdata=request.form, obj=budget_item)
        if request.method == 'POST' and form.validate:
            save_budget_changes(budget_item, form)
            return redirect(url_for("main.current_budget"))
        return render_template('budget_edit.html', form=form)
    else:
        return f'Error Loading #{id}'

#@main.route('/budgetchanges', methods=['GET','POST'])
def save_budget_changes(budgetitem, form, new=False):
    # Display the previous changes to the budget
    # Display the debits associated with the budget
    # return render_template('budgetchanges.html')
    budget = Budget()
    budget.lineitem = form.lineitem.data
    budget.amount = form.amount.data
    budget.flexible = form.flexible.data
    budget.notes = form.notes.data

    if new:
        db.session.add(budget)
    else:
        budget.id = budgetitem.id
        print(budget.id, budget.lineitem)
    db.session.commit()


@main.route('/blog', methods=['GET', 'POST'])
def blog_posts():
    # Placeholder for blog
    pass
