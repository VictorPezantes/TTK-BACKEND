from django.contrib.auth import get_user_model
from rest_framework import serializers

from ttk_backend.apps.users.models import Role
from ttk_backend.core.serializers import AuditSerializerMixin, AbstractChoiceSerializer

User = get_user_model()


class UserSerializer(AuditSerializerMixin, serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, required=False, allow_null=True)

    class Meta(AuditSerializerMixin.Meta):
        model = User

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = super(UserSerializer, self).create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance = super(UserSerializer, self).update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    rol = AbstractChoiceSerializer()

    class Meta(AuditSerializerMixin.Meta):
        model = User
        exclude = ['password', 'groups', 'user_permissions']


class RoleSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = Role
