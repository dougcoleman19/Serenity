from django.conf.urls import url

from . import views

app_name = 'calllog'
urlpatterns = [
    # ex: /calllog/
    url(r'^$', views.index, name='index'),
    # ex: /calllog/5/
    url(r'^(?P<call_log_id>[0-9]+)/$', views.calllogdetail, name='calllogdetail'),
    # ex: /calllog/new/
    url(r'^new$', views.call_log_create, name='calllognew'),
    # ex: /calllog/edit/5
    url(r'^edit/(?P<pk>\d+)$', views.call_log_update, name='calllogupdate'),
]