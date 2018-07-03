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
    request.session['count'] == False
    if 'count' in request.session == False:
    	request.session['count'] = 1
    else:
    	request.session['count'] +=1

	#creates a random string with a specified length of 14 characters 
	rand_word = get_random_string(length=14)

	context = {
		#key must be in quotes
		"rand_word": rand_word	
	}
	return render(request,'random_word_app/index.html', context)

def reset(request):

	if 'count' in request.session == True:
		del request.session['count'] 
	return redirect("/generate")


