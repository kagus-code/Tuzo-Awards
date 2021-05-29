from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt

# Create your views here.

def landing (request):
  

  title = 'Tuzo-Awards'
  return render (request,'index.html',{'title':title,}) 