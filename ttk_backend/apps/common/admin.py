from django.contrib import admin

from ttk_backend.apps.common.models import Status, DocumentType, PositionApply, EvaluationType, EvaluationCompany, \
    EvaluationClinical, ExamMedicalType, PersonaInterviewLocation
from ttk_backend.core.admin import AuditAdminMixin


@admin.register(Status)
class StatusAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(DocumentType)
class DocumentTypeAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(PositionApply)
class PositionApplyAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(EvaluationType)
class EvaluationTypeAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(EvaluationCompany)
class EvaluationCompanyAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(EvaluationClinical)
class EvaluationClinicalAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ExamMedicalType)
class ExamMedicalTypeAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(PersonaInterviewLocation)
class PersonaInterviewLocationAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name']
