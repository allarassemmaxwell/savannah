from django.apps import AppConfig

class MainAppConfig(AppConfig):
    """
    Configuration class for the MainApp Django application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    def ready(self):
        """
        Called when the Django application is ready.

        This method is used to import signals and other application-specific
        initializations that need to be set up when the application starts.
        """
        # Import signals to ensure they are registered
        import main_app.signals  # noqa: F401, C0415
