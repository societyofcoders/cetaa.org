from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
	data = {'title':'Articles'}
	return render(request,'front/blog/index.html',data)