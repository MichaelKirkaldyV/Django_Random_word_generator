from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^generate$', views.generator),
	url(r'^reset$', views.reset)
]