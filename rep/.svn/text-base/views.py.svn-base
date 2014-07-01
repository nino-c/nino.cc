from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db.models import Count

from rep.models import *

def index(request):
	
	comp = Composer.objects.annotate(num_works=Count('musicalwork')).filter(num_works__gt=0)
	template = loader.get_template('repertoire.html')
	context = RequestContext(request, {
    	'composers': comp,
    	})

	return HttpResponse(template.render(context))

def showtag(request, tag):

	comp = Composer.objects.annotate(num_works=Count('musicalwork')).filter(
		num_works__gt=0).filter(
		musicalwork__tags__in=[tag])
			
	template = loader.get_template('repertoire.html')
	context = RequestContext(request, {
    	'composers': comp,
    	})

	return HttpResponse(template.render(context))

def addtags(request):
	if request.POST:
		for k,v in request.POST.iteritems():
			if 'work' in k:
				key = int(k[4:-2])
				work = MusicalWork.objects.get(pk=key)
				work.tags.clear()
				for item in request.POST.getlist(k):
					tag = Tag.objects.get(pk=int(item))
					work.tags.add(int(item))
				work.save()

	works = MusicalWork.objects.all()
	tags = Tag.objects.all()

	template = loader.get_template('add_tags.html')
	context = RequestContext(request, {
		'works': works,
		'tags': tags,
		})

	return HttpResponse(template.render(context))

def press(request):
	template = loader.get_template('press.html')
	quotes = PressQuote.objects.all()
	context = RequestContext(request, {
		'quotes': quotes,
		})
	return HttpResponse(template.render(context))

def cds(request):
	template = loader.get_template('cds.html')
	cds = CD.objects.all()
	context = RequestContext(request, {
		'cds': cds,
		})
	return HttpResponse(template.render(context))
