"""Integration tests for Audience B model."""
import pytest
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[3] / "shared" / "insights_framework"))

from model import Model


@pytest.fixture
def model():
    return Model({"audience_id": "AUDIENCE_B", "operation": "multiplication"})


def test_multiplication_correct(model):
    assert model.train({"a": 3, "b": 4}, {}) == 12

def test_multiplication_zero(model):
    assert model.train({"a": 5, "b": 0}, {}) == 0

def test_multiplication_negative(model):
    assert model.train({"a": -3, "b": 4}, {}) == -12

def test_full_pipeline_runs(model):
    result = model.run({"a": 3, "b": 4})
    assert result is not None

def test_evaluate_valid(model):
    metrics = model.evaluate(12, {})
    assert metrics["valid"] == True
    assert metrics["audience"] == "AUDIENCE_B"
