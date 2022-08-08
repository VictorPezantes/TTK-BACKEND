from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from ttk_backend.apps.admision.models import Offer, Postulant, MedicalExam, PersonalInterview, Evaluation
from ttk_backend.apps.admision.serializers import OfferSerializer, OfferDetailSerializer, PostulantSerializer, \
    EvaluationSerializer, MedicalExamSerializer, PersonalInterviewSerializer
from ttk_backend.core.filters import FilterFieldsMixin, SerializerSetMixin


class OfferViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferDetailSerializer
    list_serializer = OfferDetailSerializer
    detail_serializer = OfferDetailSerializer
    create_serializer = OfferSerializer
    update_serializer = OfferSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['status', 'offer_creator']
    search_fields = ['title', 'description', 'requisito']


class RequestPostulantViewSet(GenericViewSet, CreateModelMixin):
    queryset = Postulant.objects.all()
    serializer_class = PostulantSerializer


class PostulantViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = Postulant.objects.all()
    serializer_class = PostulantSerializer
    list_serializer = PostulantSerializer
    detail_serializer = PostulantSerializer
    create_serializer = PostulantSerializer
    update_serializer = PostulantSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class EvaluationViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    list_serializer = EvaluationSerializer
    detail_serializer = EvaluationSerializer
    create_serializer = EvaluationSerializer
    update_serializer = EvaluationSerializer


class MedicalExamViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = MedicalExam.objects.all()
    serializer_class = MedicalExamSerializer
    list_serializer = MedicalExamSerializer
    detail_serializer = MedicalExamSerializer
    create_serializer = MedicalExamSerializer
    update_serializer = MedicalExamSerializer


class PersonalInterviewViewSet(FilterFieldsMixin, SerializerSetMixin, ModelViewSet):
    queryset = PersonalInterview.objects.all()
    serializer_class = PersonalInterviewSerializer
    list_serializer = PersonalInterviewSerializer
    detail_serializer = PersonalInterviewSerializer
    create_serializer = PersonalInterviewSerializer
    update_serializer = PersonalInterviewSerializer
