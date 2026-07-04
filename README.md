# Sales Insights Framework

Monorepo for the sales insights ML platform.

## Structure

```
sales-insights-framework/
├── shared/
│   └── insights_framework/     ← pip installable base package
│       ├── base.py             ← ModelAudience base class
│       ├── tests/              ← shared unit tests
│       └── setup.py
├── audiences/
│   ├── sbs_client/             ← SBS Client: ADDITION (a + b)
│   │   ├── config.yaml
│   │   ├── model.py            ← class Model(ModelAudience)
│   │   └── tests/
│   └── sbs_prospect/           ← SBS Prospect: MULTIPLICATION (a * b)
│       ├── config.yaml
│       ├── model.py            ← class Model(ModelAudience)
│       └── tests/
└── .github/workflows/
    ├── sbs_client_ci.yml       ← triggers on sbs-client-* branches
    ├── sbs_prospect_ci.yml     ← triggers on sbs-prospect-* branches
    └── tag_release.yml         ← triggers on tag push to prod
```

## Branch strategy

| Audience | Dev | IAT | Prod |
|---|---|---|---|
| SBS Client | sbs-client-dev | sbs-client-iat | tag: sbs-client/v*.*.* |
| SBS Prospect | sbs-prospect-dev | sbs-prospect-iat | tag: sbs-prospect/v*.*.* |

## Walkthrough

### Step 1: Feature branch
```bash
git checkout sbs-client-dev
git checkout -b feature/my-change
# make changes in audiences/sbs_client/model.py
git push origin feature/my-change
# raise PR to sbs-client-dev
```

### Step 2: PR to sbs-client-iat
```bash
# raise PR from sbs-client-dev → sbs-client-iat
# CI auto-runs: shared unit tests + sbs_client integration tests
```

### Step 3: Cut prod tag
```bash
git tag sbs-client/v1.0.0
git push origin sbs-client/v1.0.0
# tag_release.yml fires, runs tests, triggers prod
```

## Install and test locally
```bash
pip install -e shared/insights_framework
pytest shared/insights_framework/tests/ -v
cd audiences/sbs_client && pytest tests/ -v
cd audiences/sbs_prospect && pytest tests/ -v
```