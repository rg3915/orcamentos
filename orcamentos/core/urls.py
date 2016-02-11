from django.conf.urls import url
from orcamentos.core.views import Home


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    # url(r'^status/$', v.status, name='status'),
]
