# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect

from django.shortcuts import render

# Create your views here.
def index(request):
	response = "PLACERHOLDER FOR THE USERS"
	return HttpResponse(response)

def register(request):
	response = "PLACERHOLDER FOR THE REGSTIRATION FOR USERS"
	return HttpResponse(response)

def login(request):
	response = "display 'placeholder for users to login' "
	return HttpResponse(response)

def users(request):
	response = "display 'placeholder to later display all the list of users'"
	return HttpResponse(response)


def users_new(request):
	response = "display 'placeholder to later display NEW USERS'"
	return HttpResponse(response)

