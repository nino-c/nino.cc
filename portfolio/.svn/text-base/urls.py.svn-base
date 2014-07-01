from django.conf.urls import patterns, url
from portfolio import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^show/(?P<pid>[0-9]+)/', views.project_detail, name='project_detail'),
)

