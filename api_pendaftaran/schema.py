import graphene
import pendaftaran.schema

# Create code in here
class Query(pendaftaran.schema.Query, graphene.ObjectType):
    pass


class Mutation(pendaftaran.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)