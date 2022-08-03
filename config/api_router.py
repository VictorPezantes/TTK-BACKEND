from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from ttk_backend.apps.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"
urlpatterns = [
                  # Urls JWT
                  path('auth/token-auth/', obtain_jwt_token),
                  path('auth/token-refresh/', refresh_jwt_token),
                  path('auth/token-verify/', verify_jwt_token),

                  path('common/', include(('ttk_backend.apps.common.urls', 'api_common'), namespace='api_common')),
                  path('admision/',
                       include(('ttk_backend.apps.admision.urls', 'api_admision'), namespace='api_admision')),
              ] + router.urls
