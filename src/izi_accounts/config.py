from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class IZIAccountsConfig(AppConfig):
    label = 'izi_accounts'
    name = 'izi_accounts'
    verbose_name = _('Accounts')
