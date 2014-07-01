from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from portfolio.models import *


def index(request):
	projects = Project.objects.all() #.order_by("-begin_date")
	template = loader.get_template('projectlist.html')
	context = RequestContext(request, {'projects' : projects})
	return HttpResponse(template.render(context))

def project_detail(request, pid):
	project = Project.objects.get(pk=pid)
	template = loader.get_template('projectdetail.html')
	context = RequestContext(request, {'project': project,})
	return HttpResponse(template.render(context))

