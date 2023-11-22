from flask import Flask
from flask_restful import abort, Api, marshal_with, reqparse, Resource
from datetime import datetime
from models import NotificationModel
from http_status import HttpStatus
from pytz import utc


class NotificationManager:
    last_id = 0

    def __init__(self):
        self.notifications = {}

    def insert_notification(self, notification):
        self.__class__.last_id += 1
        notification.id = self.__class__.last_id
        self.notifications[self.__class__.last_id] = notification

    def get_notification(self, id2):
        return self.notifications[id2]

    def delete_notification(self, id2):
        del self.notifications[id2]

