from django.conf.urls import patterns, url
from concerts import views


urlpatterns = patterns('',
    url(r'^addconcert/', views.addconcert, name='addconcert'),
    url(r'^thanks/', views.thanks, name='thanks')
)

