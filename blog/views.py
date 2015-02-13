from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Comment,Label,PostLabels


def index(request):
	posts = Post.objects.all()

	data = []
	for post in posts:
		com = Comment.objects.filter(post_id=post.id)
		postlabel = PostLabels.objects.filter(post_id=post.id)
		data.append({'post':post,'comments':com,'labels':postlabel})


	return render(request,'front/blog/index.html',{'title':'Articles','data':data})
