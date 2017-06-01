import os

from flask import Flask, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import db
from app.models import User

app = Flask(__name__)

manager = Manager(app)
migrate = Migrate(app, db)


# controllers
@app.route('/')
def index():
    return render_template('_base.html')


@app.route('/hospital')
def hospital():
    return render_template('_hospital.html')


@app.route('/lawyer')
def lawyer():
    return render_template('_lawyer.html')


@app.route('/event')
def event():
    return render_template('_event.html')


@app.route('/contact')
def contact():
    return render_template("_contact.html")


@app.route('/post-script')
def post_script():
    return render_template("_postscript.html")


@app.route('/signup')
def signup():
    return render_template("_signup.html")


@app.route('/signup_detail')
def signup_detail():
    return render_template("_signup_detail.html")


@app.route('/login')
def login():
    return render_template("_login.html")


@app.route('/reset-password')
def reset_password():
    return render_template("_reset-password.html")


def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()
