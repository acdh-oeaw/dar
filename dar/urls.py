from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from appreg.api_views import WebAppViewSet

router = routers.DefaultRouter()
router.register(r'webapps', WebAppViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('docs/', include_docs_urls(title='API')),
    url(r'^admin/', admin.site.urls),
    url(r'^webapps/', include('appreg.urls', namespace='webapps')),
    url(r'^', include('webpage.urls', namespace='webpage')),
]

if 'bib' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^bib/', include('bib.urls', namespace='bib')),
    )

if 'sparql' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^sparql/', include('sparql.urls', namespace='sparql')),
    )

handler404 = 'webpage.views.handler404'
