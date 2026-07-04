"""
Integration tests for SBS Prospect model.
Tests full pipeline end to end using sample data.
"""
import pytest
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[3] / "shared" / "insights_framework"))

from model import Model


@pytest.fixture
def model():
    config = {
        "audience_id": "SBS_PROSPECT",
        "model_version": "1.0.0",
        "operation": "multiplication"
    }
    return Model(config)


def test_multiplication_correct(model):
    """Core test: 3 * 4 = 12."""
    assert model.train({"a": 3, "b": 4}, {}) == 12

def test_multiplication_zero(model):
    """Edge case: multiply by zero."""
    assert model.train({"a": 5, "b": 0}, {}) == 0

def test_multiplication_negative(model):
    """Edge case: negative numbers."""
    assert model.train({"a": -3, "b": 4}, {}) == -12

def test_full_pipeline_runs(model):
    """Integration: full pipeline completes without error."""
    result = model.run({"a": 3, "b": 4})
    assert result is not None

def test_evaluate_valid(model):
    """Evaluation returns valid flag for non-zero result."""
    metrics = model.evaluate(12, {"a": 3, "b": 4})
    assert metrics["valid"] == True
    assert metrics["audience"] == "SBS_PROSPECT"
