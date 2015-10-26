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
    url(r'^entes/(?P<slug>[\w-]+)/$',
        EnteDetailView.as_view(), name='entes-detail'),
    url(r'^entes/(?P<slug>[\w-]+)/perfis/$',
        PerfilArtisticoView.as_view(), name='perfis'),
    url(r'^perfis/(?P<slug>[\w-]+)/$',
        PerfilArtisticoDetailView.as_view(), name='perfis-detail'),
    url(r'^classificacoes/$', ClassificacoesListView.as_view(),
        name='classificacoes-list'),
]
