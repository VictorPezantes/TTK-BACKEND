from rest_framework import serializers

from ttk_backend.apps.common.models import Status, DocumentType, PositionApply, EvaluationType, EvaluationCompany
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
