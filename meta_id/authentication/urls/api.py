# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from meta_id.authentication.views.api import (
    UserViewSet,
    LoginView,
    ChangePasswordView,
)

router = DefaultRouter()

router.register(r'usuarios', UserViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^login/$', LoginView.as_view()),
    url(r'^password/change/(?P<user_pk>\d+)/$',
        ChangePasswordView.as_view()),
]
