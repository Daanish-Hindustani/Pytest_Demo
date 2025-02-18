import pytest
import sys
import os
from fastapi.testclient import TestClient

# Dynamically add 'src' directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from main import app  
from equation import Equation
from algebra import Algebra

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_equation():
    return Equation(10, 5, 'add')

@pytest.fixture
def sample_algebra():
    return Algebra('10x', '5x', 'multiply', 50)
