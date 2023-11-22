from flask_restful import fields

notification_fields = {
    "id": fields.Integer,
    "uri": fields.Url("notification_endpoint"),
    "message": fields.String,
    "ttl": fields.Integer,
    "creation_date": fields.DateTime,
    "notification_category": fields.String,
    "displayed_times": fields.Integer,
    "displayed_once": fields.Boolean
}

