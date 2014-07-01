from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from source.models import *
import os
import settings

def index(request):
	items = SourceCode.objects.all()
	template = loader.get_template('sourcelist.html')
	context = RequestContext(request, {'items': items})
	return HttpResponse(template.render(context))

def show_source(request, source_id):
	source = SourceCode.objects.get(pk=source_id)
	code = None
	#if source.source_file:
	#	cwd = os.path.split(os.getcwd())
	#	
	#	f = open('/home/nino')
	template = loader.get_template('viewsource.html')
	context = RequestContext(request, {'item': source})
	return HttpResponse(template.render(context))

