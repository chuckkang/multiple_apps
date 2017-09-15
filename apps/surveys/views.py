from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "PLACE HOLDER TO dISPLAY SURVEY HOMEPAGE"
	return HttpResponse(response)

def new(request):
	response = "placeholder to later TO SUBMIT SURVEY FORMS"
	return HttpResponse(response)