from django.conf.urls import url

from . import views

app_name = 'neighborhoodwatch'
urlpatterns = [
    # ex: /neighborhoodwatch/
    url(r'^$', views.index, name='index'),
    # ex: /neighborhoodwatch/5/
    url(r'^(?P<perp_id>[0-9]+)/$', views.detail, name='perpdetail'),
    # ex: /neighborhoodwatch/new/
    url(r'^new$', views.perp_create, name='perpnew'),
    url(r'^edit/(?P<pk>\d+)$', views.perp_update, name='perpupdate'),
    # url(r'^delete/(?P<pk>\d+)$', views.client_delete, name='clientdelete'),
    # url(r'^new/mini$', views.client_create_mini, name='clientnewmini'),
    # url(r'^new/success/$', views.information_received, name='informationadded'),
]