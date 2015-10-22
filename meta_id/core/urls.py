from django.conf.urls import url

from .views import (
    EnteView,
    EnteDetailView,
    ClassificacoesListView,
    PerfilArtisticoView,
    PerfilArtisticoDetailView
)

urlpatterns = [
    url(r'^entes/$', EnteView.as_view(), name='entes'),
    url(r'^entes/(?P<uid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        EnteDetailView.as_view(), name='entes-detail'),
    url(r'^entes/(?P<uid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/perfis/$',
        PerfilArtisticoView.as_view(), name='perfis'),
    url(r'^perfis/(?P<uid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        PerfilArtisticoDetailView.as_view(), name='perfis-detail'),
    url(r'^perfis/classificacoes/$', ClassificacoesListView.as_view(),
        name='classificacoes-list'),
]
