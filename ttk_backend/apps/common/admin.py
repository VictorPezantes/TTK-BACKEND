from django.contrib import admin

from ttk_backend.apps.common.models import Status, DocumentType
from ttk_backend.core.admin import AuditAdminMixin


@admin.register(Status)
class StatusAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(DocumentType)
class StatusAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']
