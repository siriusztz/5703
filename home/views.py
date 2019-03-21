from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#挂在Home界面
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#


