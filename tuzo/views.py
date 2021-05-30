from django.core.checks import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,Review
from .forms import UploadProjectForm

# Create your views here.

def landing (request):
  post =Project.objects.all()
  

  title = 'Tuzo-Awards'
  return render (request,'index.html',{'title':title,'Posts':post,})  


def upload_image(request):
  current_user = request.user
  if request.method == 'POST':
    form = UploadProjectForm(request.POST, request.Files)
    if form.is_valid():
      project = form.save(commit=False)
      project.Publisher = current_user
      project.save()
      return redirect(landing)
    else:
      form = UploadProjectForm
    return render(request, 'upload.html', {"form":form})    



