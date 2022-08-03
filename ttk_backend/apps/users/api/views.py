from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# from rest_framework_filters.backends import DjangoFilterBackend

from ttk_backend.core.filters import FilterFieldsMixin, SerializerSetMixin
from .serializers import UserSerializer, RoleSerializer, UserDetailSerializer
from ..models import Role

User = get_user_model()


class UserViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    list_serializer = UserDetailSerializer
    detail_serializer = UserDetailSerializer
    create_serializer = UserSerializer
    update_serializer = UserSerializer
    filter_backends = [SearchFilter]
    # filterset_fields = ['agency', 'rol']
    search_fields = ['name', 'email']

    @action(detail=False)
    def me(self, request):
        serializer = UserDetailSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class RoleViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    list_serializer = RoleSerializer
    detail_serializer = RoleSerializer
    create_serializer = RoleSerializer
    update_serializer = RoleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = super(RoleViewSet, self).get_queryset()
        return queryset
