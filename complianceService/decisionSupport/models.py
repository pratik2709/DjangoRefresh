from mongoengine import Document, fields

class Poll(Document):
    poll_name = fields.StringField(required=True)
    # poll_votes = fields.IntegerField(required=True)