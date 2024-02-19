from flask_restful import fields, Resource, abort, marshal_with, reqparse
from notification_manager import NotificationManager
from http_status import HttpStatus
from service import notification_manager

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


class Notification(Resource):
    def abort_if_notification_not_found(self, id):
        if id not in NotificationManager.notifications:
            abort(
                HttpStatus.not_found_404.value,
                message="Notification {0} doesn't exist.".format(id)
            )

    @marshal_with(notification_fields)
    def get(self, id):
        self.abort_if_notification_not_found(id)
        return notification_manager.get_notification(id)

    def delete(self, id):
        self.abort_if_notification_not_found(id)
        notification_manager.delete_notification(id)
        return '', HttpStatus.no_content_204.value

    @marshal_with(notification_fields)
    def patch(self, id):
        self.abort_if_notification_not_found(id)
        notification = notification_manager.get_notification(id)
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str)
        parser.add_argument("ttl", type=int)
        parser.add_argument("displayed_times", type=int)
        parser.add_argument("displayed_once", type=bool)

        args = parser.parse_args()
        print(args)
        if "message" in args and args["message"] is not None:
            notification.message = args["message"]

        if "ttl" in args and args["ttl"] is not None:
            notification.ttl = args["ttl"]

        if "displated_times" in args and args["displayed_times"] is not None:
            notification.displayed_time = args["displayed_times"]

        if "displayed_once" in args and args["displayed_once"] is not None:
            notification.displayed_once = args["displayed_once"]

        return notification
