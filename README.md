# Alliance Auth GraphQL API
# WORK IN PROGRESSS - not ready for production
# Authentication is not currently handled, if you deploy to production you are likely exposing data publicly which you do not want to do.

## Installation

1. Install the repo from git
1. `pip install graphene graphene_django`
1. add `'aagraphql'` to your `INSTALLED_APPS` in your project's `local.py`
1. add the following to your `local.py`
```python
GRAPHENE = {
    'SCHEMA': 'aagraphql.schema.schema'
}
```

