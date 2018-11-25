from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('orcamentos.core.urls', namespace='core')),
    path('crm/', include('orcamentos.crm.urls', namespace='crm')),
    path('proposal/', include('orcamentos.proposal.urls', namespace='proposal')),
    path('admin/', admin.site.urls),
]
