from rest_framework.routers import DefaultRouter

from ttk_backend.apps.admision.views import OfferViewSet, PostulantViewSet, EvaluationViewSet, \
    MedicalExamViewSet, PersonalInterviewViewSet

app_name = 'api_admision'

router = DefaultRouter()
router.register(r'offers', OfferViewSet)
router.register(r'postulants', PostulantViewSet)
router.register(r'evaluations', EvaluationViewSet)
router.register(r'medical-exams', MedicalExamViewSet)
router.register(r'personal-interviews', PersonalInterviewViewSet)
urlpatterns = router.urls
