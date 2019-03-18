import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta
from collections import OrderedDict

# After a few iterations, an article from Chris Moffitt provided a better
# direction to use a generator function to create the calcuations before
# passing it to pandas. His article can be found here:
# http://pbpython.com/amortization-model-revised.html
# OrderDict, datetime reporting


def amortize(initial_loan, interest_rate, years, start_date=date.today(),
             payments_per_year=12, payment=None, additional_payment=0):

    period = 1
    beg_balance = initial_loan
    remaining_balance = initial_loan
    total_interest = 0
    if not payment:
        payment = -round(np.pmt(interest_rate / payments_per_year,
        years * payments_per_year, beg_balance), 2)

    while remaining_balance > 0:
        interest = round(interest_rate / payments_per_year * remaining_balance,
                         2)
        principle = payment - interest
        additional_payment = min(additional_payment,
                                 (remaining_balance - principle))
        remaining_balance -= principle + additional_payment
        total_interest += interest

        yield OrderedDict([
            ('Month', start_date),
            ('Period', period),
            ('Begining Balance', beg_balance),
            ('Payment', payment),
            ('Interest', interest),
            ('Principle', principle),
            ('Additional Payment', additional_payment),
            ('Remaining Balance', remaining_balance),
            ('Total Interest Paid', total_interest)
        ])

        beg_balance = remaining_balance
        start_date
        period += 1
        start_date += relativedelta(months=+1)
