from mongoengine import Document, StringField, ListField, ReferenceField
class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    replies = ListField(ReferenceField('Reply'))
    likes = ListField(StringField())  # Store user IDs who liked the post
    def __str__(self):
        return f'Post(title={self.title}, content={self.content})'