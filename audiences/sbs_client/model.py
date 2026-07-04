"""
SBS Client model — extends ModelAudience.
Operation: ADDITION (a + b)
Override only what is specific to SBS Client.
"""
from insights_framework import ModelAudience


class Model(ModelAudience):
    """
    SBS Client pipeline.
    Inherits full pipeline from ModelAudience.
    Overrides: train() with addition logic.
    """

    def train(self, data, params):
        """
        SBS Client trains on addition.
        In real use: replace with XGBoost propensity model.
        """
        a = data.get("a", 0)
        b = data.get("b", 0)
        result = a + b
        print(f"[SBS_CLIENT] Addition: {a} + {b} = {result}")
        return result

    def evaluate(self, model, data):
        """SBS Client evaluation — checks result is positive."""
        return {
            "result": model,
            "valid": model >= 0,
            "audience": self.audience_id
        }


if __name__ == "__main__":
    import yaml, pathlib
    cfg = yaml.safe_load(
        pathlib.Path("audiences/sbs_client/config.yaml").read_text()
    )
    pipeline = Model(cfg)
    pipeline.run({"a": 10, "b": 5})
