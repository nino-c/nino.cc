from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from concerts.models import *
from rep.models import *

def addconcert(request):
	if request.method == 'POST':
		form = ConcertForm(request.POST)

		if form.is_valid():
			newconcert = form.save()
			submission = ConcertSubmission(
				concert=newconcert,
				pending=True,
				remote_ip=request.META.get('REMOTE_ADDR')
				)
			submission.save()
			return HttpResponseRedirect('thanks/')

	else:
		form = ConcertForm()
		return render(request, 'addconcert.html', {
			'form': form,
			})

def thanks(request):
	return HttpResponse('thanks') #render(request, 'page.html', {})
