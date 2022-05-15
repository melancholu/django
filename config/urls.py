from django.urls import include, path

urlpatterns = [
    path("", include("config.api_router")),
    path("", include("apps.auth.urls"), name="auth"),
    path("", include("django.contrib.auth.urls")),
]
