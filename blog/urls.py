from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
	url(r'post/(?P<slug>\w+)',views.article),
	url(r'^$',views.index,name='index'),
)