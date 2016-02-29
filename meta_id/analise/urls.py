from django.conf.urls import url

from .views import AnaliseDetailView, AnaliseListView

urlpatterns = [
    url(
        r'^(?P<id_pub>)[a-zA-Z0-9\-]/$',
        AnaliseDetailView.as_view(),
        name='entes'
        ),
    url(
        r'^$',
        AnaliseListView.as_view(),
        name='list-ente'
    ),
]
