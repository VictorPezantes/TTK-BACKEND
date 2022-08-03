from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from ttk_backend.apps.admision.models import Offer, Postulant, WorkExperience
from ttk_backend.apps.admision.serializers import OfferSerializer, OfferDetailSerializer, PostulantSerializer, \
    WorkExperienceSerializer, EvaluationSerializer
from ttk_backend.core.filters import FilterFieldsMixin, SerializerSetMixin


class OfferViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferDetailSerializer
    list_serializer = OfferDetailSerializer
    detail_serializer = OfferDetailSerializer
    create_serializer = OfferSerializer
    update_serializer = OfferSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class PostulantViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = Postulant.objects.all()
    serializer_class = PostulantSerializer
    list_serializer = PostulantSerializer
    detail_serializer = PostulantSerializer
    create_serializer = PostulantSerializer
    update_serializer = PostulantSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class WorkExperienceViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    list_serializer = WorkExperienceSerializer
    detail_serializer = WorkExperienceSerializer
    create_serializer = WorkExperienceSerializer
    update_serializer = WorkExperienceSerializer


class EvaluationViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = EvaluationSerializer
    list_serializer = EvaluationSerializer
    detail_serializer = EvaluationSerializer
    create_serializer = EvaluationSerializer
    update_serializer = EvaluationSerializer
