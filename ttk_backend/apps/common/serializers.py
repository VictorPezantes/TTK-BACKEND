from rest_framework import serializers

from ttk_backend.apps.common.models import Status, DocumentType, PositionApply, EvaluationType, EvaluationCompany, \
    EvaluationClinical, ExamMedicalType, PersonaInterviewLocation, CivilStatus, District, Province, Department
from ttk_backend.core.serializers import AuditSerializerMixin


class StatusSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = Status


class DocumentTypeSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = DocumentType


class PositionApplySerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = PositionApply


class EvaluationTypeSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = EvaluationType


class EvaluationCompanySerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = EvaluationCompany


class EvaluationClinicalSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = EvaluationClinical


class ExamMedicalTypeSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = ExamMedicalType


class PersonaInterviewLocationSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = PersonaInterviewLocation


class CivilStatusSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = CivilStatus


class DistrictSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = District


class ProvinceSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = Province


class DepartmentSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = Department
