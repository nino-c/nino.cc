from django.conf.urls import patterns, url

from rep import views


urlpatterns = patterns('',
    url(r'^repertoire/', views.index, name='index'),
    url(r'^addtags/', views.addtags, name='addtags'),
    url(r'^tag/(?P<tag>[0-9]+)/', views.showtag, name='showtag'),
    url(r'^press/', views.press, name='press'),
    url(r'^cds/', views.cds, name='cds')
)

