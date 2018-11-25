from django.urls import path
from orcamentos.core.views import home, subscription, welcome, Dashboard, status

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', subscription, name='subscription'),
    path('bemvindo/', welcome, name='welcome'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('status/', status, name='status'),
]
