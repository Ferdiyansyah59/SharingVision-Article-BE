from app import ma
from app.models.post import Post
from marshmallow import fields, validate

VALID_STATUSES = ['published', 'draft', 'trash']

class PostInputSchema(ma.Schema):
    title = fields.Str(
        required=True,
        validate=validate.Length(min=20, error='Minimum title is 20 character'),
        error_messages={'required': 'Title must be input!'}
    )

    content = fields.Str(
        required=True,
        validate=validate.Length(min=200, error='Minimum content is 200 character'),
        error_messages={'required': 'Content must be input!'}
    )

    category = fields.Str(
        required=True,
        validate=validate.Length(min=3, error='Minimum category is 3 character'),
        error_messages={'required': 'Cartegory must be input!'}
    )

    status = fields.Str(
        required=True,
        validate=validate.OneOf(
            choices=VALID_STATUSES,
            error='Status must published, draft, or trash!'
        ),
        error_messages={'required': 'Status must be input!'}
    )

class PostOutputSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True

        id = fields.Int(dump_only=True)
        created_date = fields.DateTime(dump_only=True)
        updated_date = fields.DateTime(dump_only=True)

post_input_schema = PostInputSchema()
post_output_schema = PostOutputSchema()

posts_output_Schema = PostOutputSchema(many=True)