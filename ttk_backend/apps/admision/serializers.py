from rest_framework import serializers

from ttk_backend.apps.admision.models import Offer, Postulant, Evaluation, MedicalExam, \
    PersonalInterview
from ttk_backend.core.serializers import AuditSerializerMixin, AbstractChoiceSerializer


class PostulantSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = Postulant


class OfferSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = Offer


class OfferDetailSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """
    position = AbstractChoiceSerializer()
    offer_creator = AbstractChoiceSerializer()

    class Meta(AuditSerializerMixin.Meta):
        model = Offer


class EvaluationSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = Evaluation


class MedicalExamSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = MedicalExam


class PersonalInterviewSerializer(serializers.ModelSerializer):
    """
        Serializer for Client model.
    """

    class Meta(AuditSerializerMixin.Meta):
        model = PersonalInterview
