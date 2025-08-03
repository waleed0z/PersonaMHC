from django.apps import AppConfig


class OrpheusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orpheus'

    def ready(self):
        # This is the crucial line that connects your signal handlers
            import orpheus.signals