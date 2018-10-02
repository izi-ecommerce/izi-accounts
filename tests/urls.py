from django.conf.urls import url
from django.contrib import admin
from izi.app import application

from izi_accounts.api.app import application as api_app
from izi_accounts.dashboard.app import application as accounts_app

admin.autodiscover()

urlpatterns = [
    url(r'^dashboard/accounts/', accounts_app.urls),
    url(r'^api/', api_app.urls),
    url(r'', application.urls),
]
