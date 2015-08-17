from django.conf.urls import url

from .views import RegistroListView

urlpatterns = [
    url(r'^$', RegistroListView.as_view(), name='registro-list'),
]
