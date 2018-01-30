from django.shortcuts import render			#render basically renders or give paths to any file like html file

def index(request):
	return render(request, 'personal/home.html')			#this is for returning a render to home.html

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','shushantkmr2@gmail.com']})
