from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Role


app = create_app('default')
migrate = Migrate(app, db)


# add objects to be imported by default
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


# enable running unittests
@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
