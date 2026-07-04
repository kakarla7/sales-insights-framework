"""
ModelAudience — base class for all BU model pipelines.
Each audience inherits this and overrides only what differs.
"""

class ModelAudience:
    """
    Template pipeline:
      1. explore()     — EDA
      2. tune()        — hyperparameter search
      3. train()       — model training
      4. compare()     — compare candidates
      5. select()      — pick best model
      6. evaluate()    — final evaluation
      7. rationale()   — generate rationale
      8. rules()       — apply rules engine
      9. deliver()     — Layer 4 delivery
    """

    def __init__(self, config: dict):
        self.config = config
        self.audience_id = config.get("audience_id", "UNKNOWN")

    def explore(self, data):
        """EDA — override to add audience-specific checks."""
        print(f"[{self.audience_id}] Running EDA...")
        return data

    def tune(self, data):
        """Hyperparameter tuning — override for custom param grids."""
        print(f"[{self.audience_id}] Tuning hyperparameters...")
        return {}

    def train(self, data, params):
        """Model training — override for custom model architecture."""
        print(f"[{self.audience_id}] Training model...")
        return None

    def compare(self, models):
        """Compare model candidates — override for custom metrics."""
        print(f"[{self.audience_id}] Comparing models...")
        return models

    def select(self, models):
        """Select best model — override for custom selection logic."""
        print(f"[{self.audience_id}] Selecting best model...")
        return models[0] if models else None

    def evaluate(self, model, data):
        """Evaluate model — override for audience-specific KPIs."""
        print(f"[{self.audience_id}] Evaluating model...")
        return {}

    def rationale(self, model, data):
        """Generate rationale — override for custom explanation logic."""
        print(f"[{self.audience_id}] Generating rationale...")
        return {}

    def rules(self, scores):
        """Rules engine — override for audience-specific business rules."""
        print(f"[{self.audience_id}] Applying rules engine...")
        return scores

    def deliver(self, scores):
        """Layer 4 delivery — common for all audiences."""
        print(f"[{self.audience_id}] Delivering to apps-db and Salesforce...")
        return True

    def run(self, data):
        """Full pipeline — do not override. Override individual steps."""
        data   = self.explore(data)
        params = self.tune(data)
        model  = self.train(data, params)
        models = self.compare([model])
        best   = self.select(models)
        metrics = self.evaluate(best, data)
        rationale = self.rationale(best, data)
        scores = self.rules(metrics)
        self.deliver(scores)
        print(f"[{self.audience_id}] Pipeline complete.")
        return scores

