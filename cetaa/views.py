from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	data = {'title':'CETAA'}
	return render(request,'front/index.html',data)