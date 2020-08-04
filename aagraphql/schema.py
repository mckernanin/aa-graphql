import graphene
from aagraphql.app_settings import srp_active
models_for_schema = []
if srp_active():
    import aagraphql.modules.srp.schema
    models_for_schema.append(aagraphql.modules.srp.schema.Query)

models_for_schema.append(graphene.ObjectType)


class Query(*models_for_schema):
    pass


schema = graphene.Schema(query=Query)
