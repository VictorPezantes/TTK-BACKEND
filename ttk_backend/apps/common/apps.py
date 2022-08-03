from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):
    name = "ttk_backend.apps.common"
    verbose_name = _("Commons")

    def ready(self):
        try:
            import apps.common.signals  # noqa F401
        except ImportError:
            pass
