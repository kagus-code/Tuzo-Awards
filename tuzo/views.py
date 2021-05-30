from django.core.checks import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,
from django.http  import HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,Review
from .forms import UploadProjectForm,UpdateProfileForm
from django.urls import reverse

# Create your views here.

def landing (request):
  post =Project.objects.all() 
  title = 'Tuzo-Awards'
  return render (request,'index.html',{'title':title,'Posts':post,})  


@login_required(login_url='/accounts/login/')
def user_profile (request,userId):
  projects = Project.objects.filter(Publisher=userId)
  profile = Profile.objects.filter(user=userId)
  print(profile)
  profile=Profile.objects.all()
  return render(request, 'profile/profile.html', {'posts':projects, 'profile':profile })


@login_required(login_url='/accounts/login/')
def upload_project(request):
  current_user = request.user
  if request.method == 'POST':
    form = UploadProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.Publisher = current_user
      project.save()
      return redirect(landing)
  else:
      form = UploadProjectForm
  return render(request, 'upload.html', {"form":form})    


def edit_profile(request,userId):
  old_profile = Profile.objects.filter(user=userId)
  current_user =request.user
  if request.method == 'POST':
    form= UpdateProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      if old_profile.exists():
        old_profile.delete()
        profile.user = current_user
      else:
        profile.user = current_user
      profile.email = current_user.email
      profile.save() 
      return HttpResponseRedirect(reverse('profile_page', args=[userId]))
  else:
    form = UpdateProfileForm
  return render (request, 'profile/edit_profile.html' , {"form": form})     





