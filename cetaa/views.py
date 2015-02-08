from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
	posts = Post.objects.all().filter(status=3)
	data = {'title':'CETAA','posts':posts}
	return render(request,'front/index.html',data)