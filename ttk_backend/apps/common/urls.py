from rest_framework.routers import DefaultRouter

from ttk_backend.apps.common.views import StatusViewSet, DocumentTypeViewSet, PositionApplyViewSet, \
    EvaluationCompanyViewSet, EvaluationTypeViewSet, EvaluationClinicalViewSet, ExamMedicalTypeViewSet, \
    PersonaInterviewLocationViewSet, CivilStatusSerializerViewSet, DistrictSerializerViewSet, ProvinceSerializerViewSet, \
    DepartmentSerializerViewSet

app_name = 'api_common'

router = DefaultRouter()
router.register(r'status', StatusViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'position-applies', PositionApplyViewSet)
router.register(r'evaluations-types', EvaluationTypeViewSet)
router.register(r'evaluations-companies', EvaluationCompanyViewSet)
router.register(r'evaluations-clinicals', EvaluationClinicalViewSet)
router.register(r'exam-medical-types', ExamMedicalTypeViewSet)
router.register(r'personal-interview-locations', PersonaInterviewLocationViewSet)
router.register(r'civil-status', CivilStatusSerializerViewSet)
router.register(r'districts', DistrictSerializerViewSet)
router.register(r'provinces', ProvinceSerializerViewSet)
router.register(r'departaments', DepartmentSerializerViewSet)
urlpatterns = router.urls
