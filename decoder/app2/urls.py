from django.conf.urls import url
from django.urls import path
from app2 import views

urlpatterns = [
	path('index/',views.index,name='index'),
	]
