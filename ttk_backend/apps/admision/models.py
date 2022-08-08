from datetime import datetime

from ttk_backend.apps.common.models import PositionApply, EvaluationType, EvaluationCompany, EvaluationClinical, \
    ExamMedicalType, PersonaInterviewLocation, CivilStatus, Department, Province, District
from ttk_backend.apps.users.models import User
from ttk_backend.core.models.models import AbstractAudit, AbstractChoice
from django.utils.translation import gettext_lazy as _
from django.db import models


class Postulant(AbstractChoice):

    def curricumlum_doc_file_path(self, filename):
        return f"postulants/{self.id}/curriculums/{filename}"

    def documents_doc_file_path(self, filename):
        return f"postulants/{self.id}/documents/{filename}"

    def image_file_path(self, filename):
        return f"postulants/{self.id}/images/{filename}"

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

    second_name = models.CharField(
        _('segundo nombre'),
        max_length=100,
        help_text=_("segundo nombre"),
        blank=True,
        null=True,
        default=None
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

    document_number = models.CharField(
        _('document number'),
        max_length=100,
        help_text=_("Document number"),
        blank=True,
        null=True,
        default=None
    )

    address = models.CharField(
        _('direccion'),
        max_length=100,
        help_text=_("Direccion"),
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

    secondary_email = models.EmailField(
        _('secondary email address'),
        blank=True,
        null=True,
        default=None
    )

    birth_date = models.DateField(
        _('Fecha de nacimiento'),
        null=True,
        blank=True,
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

    civil_status = models.ForeignKey(
        CivilStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    province = models.ForeignKey(
        Province,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )

    phone = models.CharField(
        _('telefono'),
        max_length=100,
        help_text=_("telefono"),
        blank=True,
        null=True,
        default=None
    )

    cellphone = models.CharField(
        _('celular'),
        max_length=100,
        help_text=_("celular"),
        blank=True,
        null=True,
        default=None
    )

    second_cellphone = models.CharField(
        _('segundo celular'),
        max_length=100,
        help_text=_("segundo celular"),
        blank=True,
        null=True,
        default=None
    )

    is_travel = models.BooleanField(
        _('disponibilidad para viajar?'),
        null=True,
        blank=True,
        default=False
    )

    is_experience = models.BooleanField(
        _('experiencia?'),
        null=True,
        blank=True,
        default=False
    )

    profession_description = models.CharField(
        _('profesion'),
        max_length=100,
        help_text=_("profesion"),
        blank=True,
        null=True,
        default=None
    )

    profesion_location = models.CharField(
        _('lugar de profesion'),
        max_length=100,
        help_text=_("lugar de profesion"),
        blank=True,
        null=True,
        default=None
    )

    profesion_last_course = models.CharField(
        _('profesion - ultimo curso realizado'),
        max_length=100,
        help_text=_("profesion - ultimo curso realizado"),
        blank=True,
        null=True,
        default=None
    )

    profesion_company = models.CharField(
        _('profesion - empresa'),
        max_length=100,
        help_text=_("profesion - empresa"),
        blank=True,
        null=True,
        default=None
    )

    work_description = models.CharField(
        _('Trabajo mas reciente'),
        max_length=100,
        help_text=_("Trabajo mas reciente"),
        blank=True,
        null=True,
        default=None
    )

    work_start = models.DateField(
        _('Fecha de ingreso'),
        null=True,
        blank=True,
        default=None
    )

    work_end = models.DateField(
        _('Fecha de salida'),
        null=True,
        blank=True,
        default=None
    )

    work_company = models.CharField(
        _('Empresa de trabajo'),
        max_length=100,
        help_text=_("Empresa de trabajo"),
        blank=True,
        null=True,
        default=None
    )

    work_exit_description = models.CharField(
        _('Motivo de salida de trabajo'),
        max_length=100,
        help_text=_("Motivo de salida de trabajo"),
        blank=True,
        null=True,
        default=None
    )

    curriculum_file = models.FileField(
        _("curriculum"),
        null=True,
        default=None,
        upload_to=curricumlum_doc_file_path,
        help_text=_("Curriculum File."),
    )

    document_file = models.FileField(
        _("document file"),
        null=True,
        default=None,
        upload_to=documents_doc_file_path,
        help_text=_("Document File."),
    )

    image_file = models.ImageField(
        _("image file"),
        null=True,
        default=None,
        upload_to=image_file_path,
        help_text=_("image File."),
    )

    class Meta:
        db_table = 'postulants'
        verbose_name = _('postulante')
        verbose_name_plural = _('postulantes')


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
        auto_now_add=True,
        help_text=_('fecha publicada'),
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
