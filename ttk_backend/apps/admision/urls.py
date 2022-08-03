from rest_framework.routers import DefaultRouter

from ttk_backend.apps.admision.views import OfferViewSet, PostulantViewSet, WorkExperienceViewSet, EvaluationViewSet

app_name = 'api_admision'

router = DefaultRouter()
router.register(r'offers', OfferViewSet)
router.register(r'postulants', PostulantViewSet)
router.register(r'work-experiences', WorkExperienceViewSet)
router.register(r'evaluations', EvaluationViewSet)
urlpatterns = router.urls
