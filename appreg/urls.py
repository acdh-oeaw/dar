from django.conf.urls import url
from . import views

app_name = 'appreg'

urlpatterns = [
    url(
        r'^apps/$',
        views.WebAppListView.as_view(),
        name='webapp_browse'
    ),
    url(
        r'^apps/detail/(?P<pk>[0-9]+)$',
        views.WebAppDetailView.as_view(),
        name='webapp_detail'
    ),
    url(
        r'^apps/create/$',
        views.WebAppCreate.as_view(),
        name='webapp_create'
    ),
    url(
        r'^apps/edit/(?P<pk>[0-9]+)$',
        views.WebAppUpdate.as_view(),
        name='webapp_edit'
    ),
    url(
        r'^apps/delete/(?P<pk>[0-9]+)$',
        views.WebAppDelete.as_view(),
        name='webapp_delete'),
]
