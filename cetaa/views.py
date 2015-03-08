from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import Post
from user.models import User
from django.conf import settings
from django.contrib.auth.models import check_password, make_password
def index(request):
	posts = Post.objects.all().filter(status=3)
	data = {'title':'CETAA','posts':posts}
	return render(request,'front/index.html',data)


def signup(request):
	try:
		check=request.session['Logged in']
	except KeyError:
		pass
	else:
		if(check):
			return HttpResponseRedirect('account')
	data = {'title':'Register for CETAA','success':0,'error':0}
	try:
		fname=request.POST['fname']
		lname=request.POST['lname']
		sex=request.POST['sex']
		dob=request.POST['dob']
		passyear=request.POST['year']
		address=request.POST['address']
		dept=request.POST['department']
		cur_job=request.POST['job']
		phone=request.POST['phone']
		contact=request.POST['contact']
		#username=request.POST['username']
		password=request.POST['pass']
		email=request.POST['email']
		admno=request.POST['admno']
		
	except Exception, e:
		data['submit']=0
	else:	
		data['submit']=1
		
		#validate data here

		try:
			u=User(fname=fname, lname=lname,sex=sex,address=address, dept=dept,cur_job=cur_job,phone=phone,password=make_password(password, salt=None, hasher='default'),email=email,admn_no=admno,passyear=passyear, contact=contact, verification=0, level=0,dob=dob)
			u.save()
		except Exception, e:
			print e
			data['error'] = 1
		else:	
			data['success']=1
			return HttpResponseRedirect('/login')

	return render(request,'front/signup.html',data)


def login(request):
	try:
		check=request.session['Logged in']
	except KeyError:
		pass
	else:
		if(check):
			return HttpResponseRedirect('/')


	data = {'title':'Login to CETAA','success':0,'error':0}
	username = 0
	password = 0
	try:
		username=request.POST['uname']
		password=request.POST['pass']
	except Exception, e:
		submit=0
	else:
		submit=1
		try:
			u=User.objects.get(email=username)
		except Exception, e:
			print e
			data['error'] = 1
			#return HttpResponse('Invalid email')
		else:
			if(check_password(password, u.password)):
				request.session['Logged in']=True
				request.session['u_id'] =u.id 
				data['success'] = 1
				return HttpResponseRedirect('account')
			else:
				data['error'] = 1
				#return HttpResponse('Wrong password')

	return render(request,'front/login.html',data)

def logout(request):
    try:
        del request.session['u_id']
        request.session['Logged in']=False
    except KeyError:
        pass
    return HttpResponse("You're logged out.")