"""
SBS Prospect model — extends ModelAudience.
Operation: MULTIPLICATION (a * b)
Override only what is specific to SBS Prospect.
"""
from insights_framework import ModelAudience


class Model(ModelAudience):
    """
    SBS Prospect pipeline.
    Inherits full pipeline from ModelAudience.
    Overrides: train() with multiplication logic.
    """

    def train(self, data, params):
        """
        SBS Prospect trains on multiplication.
        In real use: replace with XGBoost propensity model.
        """
        a = data.get("a", 0)
        b = data.get("b", 0)
        result = a * b
        print(f"[SBS_PROSPECT] Multiplication: {a} * {b} = {result}")
        return result

    def evaluate(self, model, data):
        """SBS Prospect evaluation — checks result is non-zero."""
        return {
            "result": model,
            "valid": model != 0,
            "audience": self.audience_id
        }


if __name__ == "__main__":
    import yaml, pathlib
    cfg = yaml.safe_load(
        pathlib.Path("audiences/sbs_prospect/config.yaml").read_text()
    )
    pipeline = Model(cfg)
    pipeline.run({"a": 10, "b": 5})
