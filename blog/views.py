from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


def index(request):
	posts = Post.objects.all()
	data = {'title':'Articles','posts':posts}
	return render(request,'front/blog/index.html',data)