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


class EvaluationType(AbstractChoice):
    class Meta:
        db_table = 'evaluation_type'
        verbose_name = _('tipo de evaluacion')
        verbose_name_plural = _('tipo de evaluaciones')


class EvaluationCompany(AbstractChoice):
    class Meta:
        db_table = 'evaluation_company'
        verbose_name = _('Empresa evaluadora')
        verbose_name_plural = _('Empresas evaluadoras')


class EvaluationClinical(AbstractChoice):
    class Meta:
        db_table = 'evaluation_clinical'
        verbose_name = _('Clinica evaluadora')
        verbose_name_plural = _('Clinica evaluadoras')


class ExamMedicalType(AbstractChoice):
    class Meta:
        db_table = 'exam_medical_type'
        verbose_name = _('Tipo de examen medico')
        verbose_name_plural = _('Tipos de examen medico')


class PersonaInterviewLocation(AbstractChoice):
    class Meta:
        db_table = 'personal_interview_location'
        verbose_name = _('Locacion de entrevista personal')
        verbose_name_plural = _('Locaciones de entrevista personal')
