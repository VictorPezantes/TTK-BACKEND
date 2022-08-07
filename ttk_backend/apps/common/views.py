from ttk_backend.apps.common.models import DocumentType, PositionApply, EvaluationType, EvaluationCompany, \
    Status, EvaluationClinical, ExamMedicalType, PersonaInterviewLocation, CivilStatus, District, Province, Department
from ttk_backend.apps.common.serializers import DocumentTypeSerializer, EvaluationTypeSerializer, \
    EvaluationCompanySerializer, PositionApplySerializer, EvaluationClinicalSerializer, ExamMedicalTypeSerializer, \
    PersonaInterviewLocationSerializer, CivilStatusSerializer, DistrictSerializer, ProvinceSerializer, \
    DepartmentSerializer
from ttk_backend.core.filters import FilterFieldsMixin
from ttk_backend.apps.common.serializers import StatusSerializer
from rest_framework.viewsets import ModelViewSet


class StatusViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class DocumentTypeViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class PositionApplyViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = PositionApply.objects.all()
    serializer_class = PositionApplySerializer


class EvaluationTypeViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = EvaluationType.objects.all()
    serializer_class = EvaluationTypeSerializer


class EvaluationCompanyViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = EvaluationCompany.objects.all()
    serializer_class = EvaluationCompanySerializer


class EvaluationClinicalViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = EvaluationClinical.objects.all()
    serializer_class = EvaluationClinicalSerializer


class ExamMedicalTypeViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = ExamMedicalType.objects.all()
    serializer_class = ExamMedicalTypeSerializer


class PersonaInterviewLocationViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = PersonaInterviewLocation.objects.all()
    serializer_class = PersonaInterviewLocationSerializer


class CivilStatusSerializerViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = CivilStatus.objects.all()
    serializer_class = CivilStatusSerializer


class DistrictSerializerViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class ProvinceSerializerViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class DepartmentSerializerViewSet(FilterFieldsMixin, ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
