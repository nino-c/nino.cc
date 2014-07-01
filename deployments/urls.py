from django.conf.urls import patterns, url

from deployments import views


urlpatterns = patterns('',
    url(r'^(?P<requestfile>[a-zA-Z0-9\-]+)', views.index, name='getfile'),

)

