"""
Integration tests for Audience A model.
Requires: pip install -e shared/insights_framework
Run from repo root: cd audiences/audience_a && pytest tests/ -v
"""
import pytest
import sys
import os

# Add audience_a directory to path so we can import model.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from model import Model


@pytest.fixture
def model():
    return Model({
        "audience_id": "AUDIENCE_A",
        "model_version": "1.0.0",
        "operation": "addition"
    })


def test_addition_correct(model):
    """Core test: 1 + 2 = 3."""
    assert model.train({"a": 1, "b": 2}, {}) == 3

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
    assert metrics["audience"] == "AUDIENCE_A"
