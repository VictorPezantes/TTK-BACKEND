from rest_framework import serializers

from ttk_backend.apps.common.models import Status, DocumentType, PositionApply
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
