from ttk_backend.core.models.models import AbstractChoice
from django.utils.translation import gettext_lazy as _


class Status(AbstractChoice):
    class Meta:
        db_table = 'status'
        verbose_name = _('estado')
        verbose_name_plural = _('estados')


class DocumentType(AbstractChoice):
    class Meta:
        db_table = 'document_type'
        verbose_name = _('tipo documento')
        verbose_name_plural = _('tipo de documento')


class PositionApply(AbstractChoice):
    class Meta:
        db_table = 'position_apply'
        verbose_name = _('cargo a postular')
        verbose_name_plural = _('cargos a postular')
