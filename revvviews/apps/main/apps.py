from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'revvviews.apps.main'

    def ready(self):
        from revvviews.apps.main import signals
