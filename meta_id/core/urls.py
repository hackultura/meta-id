from django.conf.urls import url

from .views import EnteListView

urlpatterns = [
    url(r'^$', EnteListView.as_view(), name='entes-list'),
]
