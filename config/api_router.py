from django.conf import settings
from django.urls import path

from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.users.views import RegisterView
from apps.users.viewsets import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

# API URLS
urlpatterns = [
    path("registration/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]

app_name = "api"
urlpatterns += router.urls
