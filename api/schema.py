import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Events as EventsModel
from models import Sources as SourcesModel


class Sources(MongoengineObjectType):
    class Meta:
        model = SourcesModel
        interfaces = (Node,)


class Events(MongoengineObjectType):
    class Meta:
        model = EventsModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_sources = MongoengineConnectionField(Sources)
    all_events = MongoengineConnectionField(Events)


schema = graphene.Schema(query=Query, types=[Sources, Events])
