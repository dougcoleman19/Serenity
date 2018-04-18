from django.conf.urls import url

from . import views

app_name = 'shelter'
urlpatterns = [
    # ex: /shelter/
    url(r'^$', views.index, name='index'),
    # ex: /clients/5/
    # url(r'^(?P<client_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^new$', views.client_create, name='clientnew'),
    url(r'^edit/(?P<pk>\d+)$', views.room_update, name='roomupdate'),
    #url(r'^update/(?P<pk>\d+)$', views.remove_client, name='removeclient'),
    # url(r'^new/mini$', views.client_create_mini, name='clientnewmini'),
    # url(r'^new/success/$', views.information_received, name='informationadded'),
]