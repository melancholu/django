from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "apps.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            from actstream import registry

            registry.register(self.get_model("User"))
        except ImportError:
            pass
