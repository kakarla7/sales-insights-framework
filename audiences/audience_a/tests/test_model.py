"""
Integration tests for SBS Client model.
Tests full pipeline end to end using sample data.
"""
import pytest
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[3] / "shared" / "insights_framework"))

from model import Model


@pytest.fixture
def model():
    config = {
        "audience_id": "SBS_CLIENT",
        "model_version": "1.0.0",
        "operation": "addition"
    }
    return Model(config)


def test_addition_correct(model):
    """Core test: 1 + 2 = 3."""
    model.train({"a": 1, "b": 2}, {}) == 3

def test_addition_zero(model):
    """Edge case: adding zero."""
    assert model.train({"a": 5, "b": 0}, {}) == 5

def test_addition_negative(model):
    """Edge case: negative numbers."""
    assert model.train({"a": -3, "b": 3}, {}) == 0

def test_full_pipeline_runs(model):
    """Integration: full pipeline completes without error."""
    result = model.run({"a": 10, "b": 5})
    assert result is not None

def test_evaluate_valid(model):
    """Evaluation returns valid flag."""
    metrics = model.evaluate(15, {"a": 10, "b": 5})
    assert metrics["valid"] == True
    assert metrics["audience"] == "SBS_CLIENT"
