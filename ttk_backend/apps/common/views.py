from ttk_backend.apps.common.models import DocumentType, PositionApply
from ttk_backend.apps.common.serializers import DocumentTypeSerializer
from ttk_backend.core.filters import FilterFieldsMixin
from ttk_backend.apps.common.models import Status
from ttk_backend.apps.common.serializers import StatusSerializer
from rest_framework.viewsets import ModelViewSet


class StatusViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class DocumentTypeViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class PositionApplyViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = PositionApply
