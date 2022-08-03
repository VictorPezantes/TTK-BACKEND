from rest_framework.routers import DefaultRouter

from ttk_backend.apps.common.views import StatusViewSet, DocumentTypeViewSet, PositionApplyViewSet

app_name = 'api_common'

router = DefaultRouter()
router.register(r'status', StatusViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'position-applies', PositionApplyViewSet)
urlpatterns = router.urls
