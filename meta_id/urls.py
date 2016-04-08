from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('meta_id.authentication.urls',
                                  namespace='auth')),
    url(r'^api/v1/', include('meta_id.core.urls', namespace='api')),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
