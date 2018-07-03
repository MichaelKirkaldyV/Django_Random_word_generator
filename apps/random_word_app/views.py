# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#the line below imports the random module into django
from django.utils.crypto import get_random_string
#must import render, redirect, HttpResponse
from django.shortcuts import render, HttpResponse, redirect

def generator(request):

	#must run the following commands in the terminal to use Sessions. 
	#python manage.py makemigrations
    #python manage.py migrate
    if not 'count' in request.session:
    	request.session['count'] = 1
    else:
    	request.session['count'] +=1	

	context = {
		#key must be in quotes
		#creates a random string with a specified length of 14 characters 
		"rand_word": get_random_string(length=14)
	}
	return render(request,'random_word_app/index.html', context)

def reset(request):
		del request.session['count'] 
		return redirect("/generate")


