from dj_rest_auth.registration.views import RegisterView as BaseRegisterView

from .serializers import RegisterSerializer


class RegisterView(BaseRegisterView):
    serializer_class = RegisterSerializer

    def get_response_data(self, user):
        data = super().get_response_data(user)
        data["access"] = data.pop("access_token")
        data["refresh"] = data.pop("refresh_token")
        return data
