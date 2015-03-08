from django.conf.urls import patterns, url

from user import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^post',views.newpost,name='newpost'),
	url(r'^view',views.viewpost,name='viewpost'),
)