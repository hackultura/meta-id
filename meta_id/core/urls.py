from django.conf.urls import url

from .views import EnteListView, ClassificacoesListView

urlpatterns = [
    url(r'^entes/$', EnteListView.as_view(), name='entes-list'),
    url(r'^perfis/classificacoes/$', ClassificacoesListView.as_view(),
        name='classificacoes-list'),
]
