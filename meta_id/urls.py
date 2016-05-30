from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from meta_id.authentication.views import RegisterView

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', RegisterView.as_view(), name='register'),

    url(r'^oauth/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/v1/auth/', include('meta_id.authentication.urls',
                                  namespace='auth')),
    url(r'^api/v1/', include('meta_id.core.urls', namespace='api')),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
