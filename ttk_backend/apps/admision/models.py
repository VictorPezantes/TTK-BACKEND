from datetime import datetime

from ttk_backend.apps.common.models import PositionApply, EvaluationType, EvaluationCompany, EvaluationClinical, \
    ExamMedicalType, PersonaInterviewLocation
from ttk_backend.apps.users.models import User
from ttk_backend.core.models.models import AbstractAudit, AbstractChoice
from django.utils.translation import gettext_lazy as _
from django.db import models


class Postulant(AbstractChoice):
    VERIFIED = 1
    PERSONAL_INTERVIEW = 2
    OUT_PROCESS = 3
    MEDICAL_EXAM = 3

    POSTULANT_STATUS = (
        (VERIFIED, 'Verificacion'),
        (PERSONAL_INTERVIEW, 'Entrevista personal'),
        (OUT_PROCESS, 'Fuera del proceso'),
        (MEDICAL_EXAM, 'Examen medico'),
    )

    status = models.IntegerField(
        _('Estado del postulante'),
        choices=POSTULANT_STATUS,
        null=True,
        blank=True,
        default=VERIFIED
    )

    last_name = models.CharField(
        _('primer apellido'),
        max_length=100,
        help_text=_("Primer apellido"),
        blank=True,
        null=True,
        default=None
    )

    sur_name = models.CharField(
        _('segundo apellido'),
        max_length=100,
        help_text=_("Segundo apellido"),
        blank=True,
        null=True,
        default=None
    )

    email = models.EmailField(
        _('email address'),
        blank=True,
        null=True,
        default=None
    )

    application_date = models.DateTimeField(
        _('Fecha postulacion'),
        null=True,
        blank=True,
        default=None
    )

    is_medical_exam = models.BooleanField(
        _('examen medico?'),
        null=True,
        blank=True,
        default=False
    )

    is_personal_interview = models.BooleanField(
        _('entrevista personal?'),
        null=True,
        blank=True,
        default=False
    )

    is_personal_interview = models.BooleanField(
        _('entrevista personal?'),
        null=True,
        blank=True,
        default=False
    )

    class Meta:
        db_table = 'postulants'
        verbose_name = _('postulante')
        verbose_name_plural = _('postulantes')


class WorkExperience(AbstractAudit):
    postulant = models.ForeignKey(
        Postulant,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    speciality = models.CharField(
        _('especialidad'),
        max_length=100,
        null=True,
        blank=True,
        default=None
    )

    company = models.CharField(
        _('empresa'),
        max_length=100,
        null=True,
        blank=True,
        default=None
    )

    init_date = models.DateTimeField(
        _('Fecha inicio'),
        null=True,
        blank=True,
        default=None
    )

    end_date = models.DateTimeField(
        _('Fecha fin'),
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        db_table = 'work_experience'
        verbose_name = _('experiencia laboral')
        verbose_name_plural = _('experiencia laboral')


class Offer(AbstractAudit):
    PENDING = 1
    APROVED = 2
    REJECTED = 3

    OFFER_STATUS = (
        (PENDING, 'Pendiente'),
        (APROVED, 'Aprobada'),
        (REJECTED, 'Rechazada')
    )

    title = models.CharField(
        _('Titulo de la oferta'),
        max_length=100,
        null=True,
        blank=True,
        default=None
    )

    description = models.TextField(
        _('Descripcion de la oferta'),
        null=True,
        blank=True,
        default=None
    )

    position = models.ForeignKey(
        PositionApply,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    requisito = models.TextField(
        _('Requisitos de la oferta'),
        null=True,
        blank=True,
        default=None
    )

    status = models.IntegerField(
        _('Estado de la oferta'),
        choices=OFFER_STATUS,
        null=True,
        blank=True,
        default=PENDING
    )

    deactivation_date = models.DateTimeField(
        _('Desactivacion de la oferta'),
        null=True,
        blank=True,
        default=None
    )

    publication_date = models.DateTimeField(
        _('Publicacion de la oferta'),
        null=True,
        blank=True,
        default=None
    )

    offer_creator = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        db_table = 'offers'
        verbose_name = _('oferta')
        verbose_name_plural = _('ofertas')

    @property
    def cantidad_postulantes(self):
        return 0


class EvaluationAbstract(AbstractAudit):
    PROGRAMED = 1
    APROVED = 2
    CANCELLED = 3
    DESAPROVED = 4

    EVALUATION_STATUS = (
        (PROGRAMED, 'Programado'),
        (APROVED, 'Aprobado'),
        (CANCELLED, 'Cancelado'),
        (DESAPROVED, 'Desaprobado'),
    )

    status = models.IntegerField(
        _('Estado de la evaluacion'),
        choices=EVALUATION_STATUS,
        null=True,
        blank=True,
        default=PROGRAMED
    )

    programed_date = models.DateTimeField(
        _('Fecha programada'),
        null=True,
        blank=True,
        default=None
    )

    postulant = models.ForeignKey(
        Postulant,
        related_name='postulant_%(model_name)ss',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    assigned = models.ForeignKey(
        User,
        related_name='assigned_%(model_name)ss',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    observations = models.TextField(
        _('Observaciones del postulante'),
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        abstract = True


class Evaluation(EvaluationAbstract):
    evaluation_type = models.ForeignKey(
        EvaluationType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    evaluation_company = models.ForeignKey(
        EvaluationCompany,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        db_table = 'evaluations'
        verbose_name = _('evaluacion')
        verbose_name_plural = _('evaluaciones')


class MedicalExam(EvaluationAbstract):
    clinical = models.ForeignKey(
        EvaluationClinical,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    exam_type = models.ForeignKey(
        ExamMedicalType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        db_table = 'medical_exams'
        verbose_name = _('examen medico')
        verbose_name_plural = _('examenes medicos')


class PersonalInterview(EvaluationAbstract):
    location = models.ForeignKey(
        PersonaInterviewLocation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        db_table = 'personal_interview'
        verbose_name = _('entrevista personal')
        verbose_name_plural = _('entrevistas personales')
