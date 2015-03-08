from django.shortcuts import render

# Create your views here.

def index(request):
	data = {'title':'My Account'}
	return render(request,'front/user/account.html',data)


def newpost(request):
	data = {'title':'New Post'}




	return render(request,'front/user/newpost.html',data)


def viewpost(request):
	data = {'title':'View Posts'}
	return render(request,'front/user/account.html',data)