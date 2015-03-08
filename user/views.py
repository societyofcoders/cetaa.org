from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from blog.models import Post
from user.models import User
# Create your views here.

def index(request):
	try:
		check=request.session['Logged in']
	except KeyError:
		pass
	else:
		if(not check):
			return HttpResponseRedirect('/login')
	data = {'title':'My Account'}
	return render(request,'front/user/account.html',data)


def newpost(request):
	try:
		check=request.session['Logged in']
	except KeyError:
		pass
	else:
		if(not check):
			return HttpResponseRedirect('/login')
	data = {'title':'New Post'}
	try:
		title=request.POST['title']
		body=request.POST['body']
		slug=request.POST['slug']
		status=request.POST['status']
	except Exception, e:
		data['submit']=0
	else:
		data['submit']=1
		p=Post(title=title, body=body, slug=slug, status=status, created=timezone.now(), modified=timezone.now(), uid=User.objects.get(id=request.session['u_id']))
		p.save()
	return render(request,'front/user/newpost.html',data)


def viewpost(request):
	try:
		check=request.session['Logged in']
	except KeyError:
		pass
	else:
		if(not check):
			return HttpResponseRedirect('/login')
	data = {'title':'View Posts'}
	return render(request,'front/user/account.html',data)