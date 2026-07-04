"""
Integration tests for Audience B model.
Requires: pip install -e shared/insights_framework
Run from repo root: cd audiences/audience_b && pytest tests/ -v
"""
import pytest
import sys
import os

# Add audience_b directory to path so we can import model.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from model import Model


@pytest.fixture
def model():
    return Model({
        "audience_id": "AUDIENCE_B",
        "model_version": "1.0.0",
        "operation": "multiplication"
    })


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
    assert metrics["audience"] == "AUDIENCE_B"
