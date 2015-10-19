from django.conf.urls import url

from .views import EnteView, ClassificacoesListView

urlpatterns = [
    url(r'^entes/$', EnteView.as_view(), name='entes'),
    url(r'^perfis/classificacoes/$', ClassificacoesListView.as_view(),
        name='classificacoes-list'),
]
