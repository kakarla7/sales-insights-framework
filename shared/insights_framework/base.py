"""
ModelAudience — base class for all BU model pipelines.
Each audience inherits this and overrides only what differs.
"""


class ModelAudience:
    """
    Template pipeline:
      explore() → tune() → train() → compare() → select()
      → evaluate() → rationale() → rules() → deliver()
    """

    def __init__(self, config: dict):
        self.config = config
        self.audience_id = config.get("audience_id", "UNKNOWN")

    def explore(self, data):
        print(f"[{self.audience_id}] Running EDA...")
        return data

    def tune(self, data):
        print(f"[{self.audience_id}] Tuning hyperparameters...")
        return {}

    def train(self, data, params):
        print(f"[{self.audience_id}] Training model...")
        return None

    def compare(self, models):
        print(f"[{self.audience_id}] Comparing models...")
        return models

    def select(self, models):
        print(f"[{self.audience_id}] Selecting best model...")
        return models[0] if models else None

    def evaluate(self, model, data):
        print(f"[{self.audience_id}] Evaluating model...")
        return {}

    def rationale(self, model, data):
        print(f"[{self.audience_id}] Generating rationale...")
        return {}

    def rules(self, scores):
        print(f"[{self.audience_id}] Applying rules engine...")
        return scores

    def deliver(self, scores):
        print(f"[{self.audience_id}] Delivering to apps-db and Salesforce...")
        return True

    def run(self, data):
        """Full pipeline — do not override. Override individual steps."""
        data     = self.explore(data)
        params   = self.tune(data)
        model    = self.train(data, params)
        models   = self.compare([model])
        best     = self.select(models)
        metrics  = self.evaluate(best, data)
        self.rationale(best, data)
        scores   = self.rules(metrics)
        self.deliver(scores)
        print(f"[{self.audience_id}] Pipeline complete.")
        return scores
