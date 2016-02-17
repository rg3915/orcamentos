from django.conf.urls import url
from orcamentos.core.views import Home, status


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^status/$', status, name='status'),
]
