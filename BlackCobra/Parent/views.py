from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	identity = "Home"
	home_data = {}
	home_data['page'] = identity
	home_data['path'] = []
	if identity not in home_data['path']:
		home_data['path'].append(identity)
	return render(request, 'home.html', home_data)