from django.apps import AppConfig
from django.conf import settings


class SlackConfig(AppConfig):
    name = 'django_slack_app'

__import__(settings.SLACK_EVENTS)