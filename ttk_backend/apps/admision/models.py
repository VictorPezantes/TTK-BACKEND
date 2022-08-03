from ttk_backend.core.models.models import AbstractChoice
from django.utils.translation import gettext_lazy as _


class Offers(AbstractChoice):
    class Meta:
        db_table = 'offers'
        verbose_name = _('oferta')
        verbose_name_plural = _('ofertas')
