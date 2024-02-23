from app import app
import pytest
import os
from app.utils.database import db

@pytest.fixture
def test_app():
    '''test application setup'''
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"

    with app.test_client() as client:
        yield client
