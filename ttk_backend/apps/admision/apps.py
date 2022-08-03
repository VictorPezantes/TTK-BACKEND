from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdmisionConfig(AppConfig):
    name = ""
    verbose_name = _("Admision")

    def ready(self):
        try:
            import apps.admision.signals  # noqa F401
        except ImportError:
            pass
