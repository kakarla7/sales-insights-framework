# sales-insights-framework

Single monorepo. Three sets of branches — shared, audience-a, audience-b.

## Branch structure

| Branch set | Branches | Owns |
|---|---|---|
| Shared | shared-dev, shared-iat, shared-prod | shared/insights_framework |
| Audience A | audience-a-dev, audience-a-iat, audience-a-prod | audiences/audience_a/ + shared/ (auto-synced) |
| Audience B | audience-b-dev, audience-b-iat, audience-b-prod | audiences/audience_b/ + shared/ (auto-synced) |

## What lives on each branch

**shared-*** branches:
```
shared/
  setup.py
  VERSION
  insights_framework/
    __init__.py
    base.py
    tests/
.github/workflows/
  shared_ci.yml
  shared_auto_tag.yml
  sync_shared_to_audiences.yml
```

**audience-a-*** branches:
```
shared/                        ← auto-synced from shared branches
audiences/audience_a/
  model.py                     ← class Model(ModelAudience)
  config.yaml
  VERSION
  tests/
.github/workflows/
  audience_a_ci.yml
  audience_a_auto_tag.yml
  audience_a_revert_shared.yml
```

**audience-b-*** branches: same pattern, audience_b only.

## How it works

### Shared changes
```
shared-dev → PR → shared-iat → CI runs → PR → shared-prod
  → auto tag: shared-v1.0.1
  → auto sync shared/ to audience-a-iat + audience-b-iat
  → auto sync shared/ to audience-a-prod + audience-b-prod
  → each audience CI runs
  → pass: audience tag cut automatically
  → fail: shared/ reverted on that audience branch, alert fires
```

### Audience changes
```
feature → PR → audience-a-dev → PR → audience-a-iat → CI runs
  → PR → audience-a-prod
  → auto tag: shared-v1.0.0--audience-a-v1.1.0
  → Databricks deploys
```

### Tag format
```
shared-v1.0.0                          ← shared release
shared-v1.0.0--audience-a-v1.1.0      ← audience-a release
shared-v1.0.0--audience-b-v2.0.0      ← audience-b release
```

## Install and test locally
```bash
pip install -e shared/
pytest shared/insights_framework/tests/ -v

PYTHONPATH=audiences/audience_a pytest audiences/audience_a/tests/ -v
PYTHONPATH=audiences/audience_b pytest audiences/audience_b/tests/ -v
```
