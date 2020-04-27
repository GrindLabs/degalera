import mongoengine


class SourceBlock(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    path = mongoengine.StringField(required=True)


class SourceField(mongoengine.EmbeddedDocument):
    key = mongoengine.StringField(required=True)
    path = mongoengine.StringField(required=True)


class Sources(mongoengine.Document):
    meta = {'collection': 'sources'}
    name = mongoengine.StringField(required=True)
    alias = mongoengine.StringField(required=True)
    logo = mongoengine.URLField(required=True)
    lookup = mongoengine.ListField(mongoengine.StringField())
    blocks = mongoengine.EmbeddedDocumentListField(SourceBlock, required=True)
    fields = mongoengine.EmbeddedDocumentListField(SourceField, required=True)
    domain = mongoengine.StringField(required=True)
    is_active = mongoengine.BooleanField(db_field='isActive', required=True)


class Events(mongoengine.Document):
    meta = {'collection': 'events'}
    name = mongoengine.StringField(required=True)
    location = mongoengine.StringField(required=True)
    date = mongoengine.DateField(required=True)
    flyer = mongoengine.URLField(required=True)
    link = mongoengine.URLField(required=True)
    description = mongoengine.StringField(required=True)
    lowest_price_ticket = mongoengine.FloatField(
        db_field='lowestPriceTicket', required=True)
    tags = mongoengine.ListField(mongoengine.StringField())
    source = mongoengine.ReferenceField(
        Sources, db_field='sourceId', required=True)
    is_carnival = mongoengine.BooleanField(
        db_field='isCarnival', required=True)
    created_at = mongoengine.DateTimeField(db_field='createdAt')
