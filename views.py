from django.http import HttpResponse

def index(resquest):
	return HttpResponse("index")

def login(request):
	return HttpResponse("login")
