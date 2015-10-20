from django.conf.urls import url

from .views import EnteView, ClassificacoesListView, PerfilArtisticoView

urlpatterns = [
    url(r'^entes/$', EnteView.as_view(), name='entes'),
    url(r'^entes/(?P<uid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/perfis/$',
        PerfilArtisticoView.as_view(), name='perfis'),
    url(r'^perfis/classificacoes/$', ClassificacoesListView.as_view(),
        name='classificacoes-list'),
]
