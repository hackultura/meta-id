# -*- coding: utf-8 -*-
from django.conf.urls import url

from meta_id.authentication.views.oauth import (
    RegisterView,
    DeveloperRegisterView,
    ApplicationList,
    ApplicationNew,
    ApplicationDetail,
    ApplicationUpdate,
    ApplicationDelete,
)

urlpatterns = (
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^developer/registro/$', DeveloperRegisterView.as_view(),
        name='developer_register'),

    url(r'^developer/aplicacoes/$',
        ApplicationList.as_view(), name="app_list"),
    url(r'^developer/aplicacoes/novo/$',
        ApplicationNew.as_view(), name="app_register"),
    url(r'^developer/aplicacoes/(?P<pk>\d+)/$',
        ApplicationDetail.as_view(), name="app_detail"),
    url(r'^developer/aplicacoes/(?P<pk>\d+)/remover/$',
        ApplicationDelete.as_view(), name="app_delete"),
    url(r'^developer/aplicacoes/(?P<pk>\d+)/atualizar/$',
        ApplicationUpdate.as_view(), name="app_update"),
)
