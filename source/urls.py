from django.conf.urls import patterns, url
from source import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^show/(?P<source_id>[0-9]+)/', views.show_source, name='show_source'),
)

