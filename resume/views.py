from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from resume.models import *

def index(request):

	resume = Resume.objects.get(pk=1)

	template = loader.get_template('resume.html')
	context = RequestContext(request, {
    	'resume': resume,
    	})

	return HttpResponse(template.render(context))