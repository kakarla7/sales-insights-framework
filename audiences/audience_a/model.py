"""
Audience A model — extends ModelAudience.
Operation: ADDITION (a + b)
"""
from insights_framework import ModelAudience


class Model(ModelAudience):
    """
    Audience A pipeline.
    Overrides: train() with addition logic.
    """

    def train(self, data, params):
        a = data.get("a", 0)
        b = data.get("b", 0)
        result = a + b
        print(f"[AUDIENCE_A] Addition: {a} + {b} = {result}")
        return result

    def evaluate(self, model, data):
        return {
            "result": model,
            "valid": model >= 0,
            "audience": self.audience_id
        }


if __name__ == "__main__":
    import yaml, pathlib
    cfg = yaml.safe_load(
        pathlib.Path("audiences/audience_a/config.yaml").read_text()
    )
    pipeline = Model(cfg)
    pipeline.run({"a": 10, "b": 5})
