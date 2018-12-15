from django.urls import path
from .views import hammer
urlpatterns = [
	path('', hammer, name='hammer')
]