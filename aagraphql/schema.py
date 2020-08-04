import graphene
import aagraphql.modules.srp.schema


class Query(aagraphql.modules.srp.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
