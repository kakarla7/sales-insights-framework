"""Unit tests for ModelAudience base class."""
import pytest
from insights_framework import ModelAudience


class DummyModel(ModelAudience):
    def train(self, data, params):
        return "dummy_model"
    def evaluate(self, model, data):
        return {"score": 0.9}


def test_pipeline_runs():
    m = DummyModel({"audience_id": "TEST"})
    result = m.run({"numbers": [1, 2, 3]})
    assert result is not None

def test_audience_id():
    m = DummyModel({"audience_id": "SBS_CLIENT"})
    assert m.audience_id == "SBS_CLIENT"

def test_deliver_returns_true():
    m = DummyModel({"audience_id": "TEST"})
    assert m.deliver({}) is True
