from rest_framework import serializers


class AuditSerializerMixin:
    """
    Mixin that excludes the audit fields from serializers.
    """

    class Meta:
        exclude = ['creation_date', 'created_by', 'update_date', 'update_by']


class AbstractChoiceSerializer(serializers.Serializer):
    """
    ListSerializer for AbstractChoice model.
    """
    id = serializers.IntegerField(allow_null=True)
    name = serializers.CharField()
    is_active = serializers.BooleanField(allow_null=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
