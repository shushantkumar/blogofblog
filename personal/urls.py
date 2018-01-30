from django.conf.urls import url
from . import views									# here . means from this folder

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact')
	]			#here we dont modify the path and then we return views.index
