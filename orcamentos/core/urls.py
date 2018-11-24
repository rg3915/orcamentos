from django.conf.urls import url
from orcamentos.core.views import home, subscription, welcome, Dashboard, status

app_name = 'core'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/$', subscription, name='subscription'),
    url(r'^bemvindo/$', welcome, name='welcome'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^status/$', status, name='status'),
]
