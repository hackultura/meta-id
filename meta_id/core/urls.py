from django.conf.urls import url

from .views import (
    EnteView,
    EnteDetailView,
    ClassificacoesListView,
    AtuacoesListView,
    PerfilArtisticoView,
    PerfilArtisticoDetailView,
    PortfolioDetailView,
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
        PortfolioDetailView.as_view(), name='portfolios-detail'),
    url(r'^atuacoes/$', AtuacoesListView.as_view(),
        name='atuacoes-list'),
    url(r'^classificacoes/$', ClassificacoesListView.as_view(),
        name='classificacoes-list'),
]
