from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "placeholder to later display all the list of blogs"
	return HttpResponse(response)

def new(request):
	response = "THIS IS THE NEW PAGE"
	return HttpResponse(response)

def create(request):
	# redirect to blogs	
	return redirect("/")

def show(request, number):
	print number
	response = 'placeholder to display blog ' + number + ' THSI IS TEH SHow METHOD'
	return HttpResponse(response)

def edit(request, number):
	response =  number + "NUMBER PAGE EDIT PAGE"
	return HttpResponse(response)

def destroy(request, number):
	response = "DESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROYDESTROY"
	return HttpResponse(response)