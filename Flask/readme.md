# Flask Website ReadMe

The main goal of this website was to further develop my understanding of Python and get a better awareness of the ins and outs of the front-end and back end of a website.  I initially followed a tutorial that provided some examples in implementing the front and back end to implement a website that allows users to sign-up, create blog posts, comment and follow bloggers, and basic user authentication and authorization.  The example website was created following the turtorials provided in Flask Web Development, 2nd Edition by Miguel Grinber (O'Reilly Media).  This is not that website.  This is a stripped down version with plans to add additional areas to provide learning opportunities using Python and Flask.  To run this website, set the environment variable to home.py, then run flask. EG:

 - set FLASK_APP=home.py
 - flask run

Future improvements can include:
 - update documentation
 - clean up the CSS or find a new template
 - add a database backend
 - add the weather app to the website
 - add in static web pages

## Amoritization
The Amoritization page is a mortgage amoritzation calculator.  This will take an input for your mortgage, then use pandas to calculate the remaining payments on your loan.

Improvements:
- Allow a payment to be used as input, so that the mortgage calc can take place mortgage payments start
- Backtrack estimated payments, interest, and years since start of mortgage if a payment amount is put in
- Allow multiple amounts to be put in for "Additional Amounts" to run a comparison
- Allow option to show only final payoff summarization
- Implement a graph to show default or compare the additional options
