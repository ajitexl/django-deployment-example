from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import base64
from app2.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):

	webpages_list = AccessRecord.objects.order_by('date')
	#$data_dict = {'access_records' : webpages_list}

	my_dict = {'insert_me' : "Hellow I am base64 decoder",'access_records' : webpages_list}


	return render(request,'app2/index.html',context=my_dict)

def thanks(request):

	import base64,re

	s=request.POST['base64']
	print(s)
	data={}

	if (len(s) % 4 == 0) and re.match('^[A-Za-z0-9+/]+[=]{0,2}$', s):

		k= str(base64.b64decode(s))

		data = {'data' : k}
		#print(data)
	else:
		#print('Wrong Input Please Give BASE64 Encoded String')
		data = {'error' :'Wrong Input Please Give BASE64 Encoded String'}

	return render(request,'app2/thanks.html',context=data)
	

