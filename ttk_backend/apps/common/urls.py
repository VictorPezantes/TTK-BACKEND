from rest_framework.routers import DefaultRouter

from ttk_backend.apps.common.views import StatusViewSet, DocumentTypeViewSet, PositionApplyViewSet, \
    EvaluationCompanyViewSet, EvaluationTypeViewSet

app_name = 'api_common'

router = DefaultRouter()
router.register(r'status', StatusViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'position-applies', PositionApplyViewSet)
router.register(r'evaluations-types', EvaluationTypeViewSet)
router.register(r'evaluations-companies', EvaluationCompanyViewSet)
urlpatterns = router.urls
