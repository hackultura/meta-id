from django.conf.urls import url

from .views import (
    EnteView,
    EnteDetailView,
    ClassificacoesListView,
    AtuacoesListView,
    PerfilArtisticoView,
    PerfilArtisticoDetailView,
    PortfolioView,
    DocumentoView,
    DocumentoDetailView,
)

urlpatterns = [
    url(r'^entes/$', EnteView.as_view(), name='entes'),
    url(r'^entes/(?P<slug>[\w-]+)/$',
        EnteDetailView.as_view(), name='entes-detail'),
    url(r'^entes/(?P<slug>[\w-]+)/perfis/$',
        PerfilArtisticoView.as_view(), name='perfis'),
    url(r'^perfis/(?P<slug>[\w-]+)/$',
        PerfilArtisticoDetailView.as_view(), name='perfis-detail'),
    url(r'^perfis/(?P<slug>[\w-]+)/portfolios/(?P<type>[\w]+)$',
        PortfolioView.as_view(), name='portfolios-detail'),
    url(r'^atuacoes/$', AtuacoesListView.as_view(),
        name='atuacoes-list'),
    url(r'^classificacoes/$', ClassificacoesListView.as_view(),
        name='classificacoes-list'),
    url(r'^documentos/$',
        DocumentoView.as_view(), name='documents'),
    url(r'^documentos/(?P<uid>[a-zA-Z0-9\-]+)/$',
        DocumentoDetailView.as_view(), name='documents-detail'),
]
