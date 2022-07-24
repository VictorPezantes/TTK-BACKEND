from django.urls import path, include

from rest_framework.routers import DefaultRouter

# Djangp REST JWT
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = DefaultRouter()
app_name = "api"

urlpatterns = [
    path('', include(('ttk_backend.apps.users.urls', 'users'), namespace='users')),

    # Urls JWT
    path('auth/token-auth/', obtain_jwt_token),
    path('auth/token-refresh/', refresh_jwt_token),
    path('auth/token-verify/', verify_jwt_token),
] + router.urls
