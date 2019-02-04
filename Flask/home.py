import os
from flask_migrate import Migrate
from app import create_app, db
# from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_contect():
    pass


@app.cli.command()
def test():
    pass
