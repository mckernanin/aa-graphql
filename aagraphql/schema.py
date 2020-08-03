import graphene

from modules.srp.schema


class Query(modules.srp.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
