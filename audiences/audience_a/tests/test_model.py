"""Integration tests for Audience A model."""
import pytest
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[3] / "shared" / "insights_framework"))

from model import Model


@pytest.fixture
def model():
    return Model({"audience_id": "AUDIENCE_A", "operation": "addition"})


def test_addition_correct(model):
    assert model.train({"a": 1, "b": 2}, {}) == 3

def test_addition_zero(model):
    assert model.train({"a": 5, "b": 0}, {}) == 5

def test_addition_negative(model):
    assert model.train({"a": -3, "b": 3}, {}) == 0

def test_full_pipeline_runs(model):
    result = model.run({"a": 10, "b": 5})
    assert result is not None

def test_evaluate_valid(model):
    metrics = model.evaluate(15, {})
    assert metrics["valid"] == True
    assert metrics["audience"] == "AUDIENCE_A"
