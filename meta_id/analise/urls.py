from django.conf.urls import url

from .views import AnaliseView

urlpatterns = [
    url(r'^analises/$', AnaliseView.as_view(), name='analises'),
    url(r'^analises/ente/(?P<id_pub>)[a-zA-Z0-9\-]+)/$', AnaliseListView.as_view(), name='list-ente')
    # url(r'^classificacoes/$', ClassificacoesListView.as_view(),
    #     name='classificacoes-list'),
    # url(r'^documentos/$',
    #     DocumentoView.as_view(), name='documents'),
    # url(r'^documentos/(?P<uid>[a-zA-Z0-9\-]+)/$',
    #     DocumentoDetailView.as_view(), name='documents-detail'),
]
