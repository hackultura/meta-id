from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('meta_id.core.urls', namespace='api')),
    url(r'^api/vi/analises', include('meta_id.analise.urls', namespace='analise')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


)
