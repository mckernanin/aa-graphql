# Alliance Auth GraphQL API
# WORK IN PROGRESSS - not ready for production
# Authentication is not currently handled, if you deploy to production you are likely exposing data publicly which you do not want to do.

## Installation

1. Install the repo from git
2. add `'aagraphql',` and `'graphene_django',` to your `INSTALLED_APPS` in your project's `local.py`
3. add the following to your `local.py`
```python
GRAPHENE = {
    'SCHEMA': 'aagraphql.schema.schema'
}
```

