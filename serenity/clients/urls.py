from django.conf.urls import url

from . import views

app_name = 'clients'
urlpatterns = [
    # ex: /clients/
    url(r'^$', views.index, name='index'),
    # ex: /clients/5/
    url(r'^(?P<client_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new$', views.client_create, name='clientnew'),
    url(r'^edit/(?P<pk>\d+)$', views.client_update, name='clientupdate'),
    url(r'^delete/(?P<pk>\d+)$', views.client_delete, name='clientdelete'),
    url(r'^new/mini$', views.client_create_mini, name='clientnewmini'),
    url(r'^new/success/$', views.information_received, name='informationadded'),
]