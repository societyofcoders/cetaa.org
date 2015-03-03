from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
	posts = Post.objects.all().filter(status=3)
	data = {'title':'CETAA','posts':posts}
	return render(request,'front/index.html',data)


def signup(request):
	data = {'title':'Register for CETAA'}
	request.method
	return render(request,'front/signup.html',data)
