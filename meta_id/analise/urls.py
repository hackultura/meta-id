from django.conf.urls import url

from .views import AnaliseEnteView, AnaliseListView

urlpatterns = [
    url(
        r'^(?P<id_pub>)[a-zA-Z0-9\-]/$',
        AnaliseEnteView.as_view(),
        name='entes'
        ),
    url(
        r'^$',
        AnaliseListView.as_view(),
        name='list-ente'
    ),
]
