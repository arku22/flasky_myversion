import unittest
from app import create_app, db
from flask import current_app


class BasicsTestCase(unittest.TestCase):

    # method to setup the environment to enable testing - run before a test
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    # method to clear objects from "setUp" method - run after a test
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # NOTE: All tests start with the prefix "test_"
    # Simple Test 1 - check if app instance is running
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # Simple Test 2 - check if app is running the 'testing' configuration
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
