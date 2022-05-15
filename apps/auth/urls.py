# from django.conf import settings
# from dj_rest_auth.jwt_auth import get_refresh_view
from django.urls import path

from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    # generate_nonce is like register view
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
]
