from django.conf.urls import url
from orcamentos.core.views import Home, registration, status


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^status/$', status, name='status'),
]
