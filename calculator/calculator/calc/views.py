from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def calc(request):
	field1 = request.GET['field1']
	field2 = request.GET['field2']
	operation = request.GET['optradio']
	result=0
	if(operation=='+'):
		result = int(field1)+int(field2)
	if(operation=='-'):
		result = int(field1)-int(field2)
	if(operation=='*'):
		result = int(field1)*int(field2)
	if(operation=='/'):
		result = int(field1)/int(field2)
	return render(request,'calc/calc.html',{'result':result})
def home(request):
	return render(request,'calc/home.html')