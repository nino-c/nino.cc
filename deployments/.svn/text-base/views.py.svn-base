from django.http import HttpResponse
import os

def index(request, requestfile):
	pwd = os.path.dirname(os.path.abspath(__file__))
	rf = pwd+'/files/'+requestfile
	if os.path.exists(rf):
		fname = rf
	elif os.path.exists(rf+'.html'):
		fname = rf+'.html'
	else: 
		return HttpResponse("can't find yer file")

	f = open(fname, 'r')
	r = f.read()
	f.close()
	return HttpResponse(r)
