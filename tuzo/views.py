from django.core.checks import messages
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from django.shortcuts import render,redirect
from django.http  import HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .models import Project,Profile,Review
from .forms import UploadProjectForm,UpdateProfileForm,RateForm
from django.urls import reverse


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializers
from rest_framework import status

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

@login_required(login_url='/accounts/login/')
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
      profile.user_name=current_user.username
      profile.save() 
      return HttpResponseRedirect(reverse('profile_page', args=[userId]))
  else:
    form = UpdateProfileForm
  return render (request, 'profile/edit_profile.html' , {"form": form})     



def search_results(request):
  if 'project' in request.GET and  request.GET["project"]:
    search_term = request.GET.get("project")
    searched_projects = Project.search_projects(search_term)
    message =f"{search_term}"

    return render(request, 'search.html', {"message":message, "posts":searched_projects,})

  else:
    message = "You havent searched for any projects"

  return render(request, 'search.html', {"message":message})


@login_required(login_url='/accounts/login/')
def rate_project(request,project_id):
    project = Project.objects.get(pk=project_id)
    reviews = Review.objects.filter(project=project_id)
    user = request.user
    design_avg =reviews.aggregate(Avg('design')).get('design__avg', 0.00)
    usability_avg =reviews.aggregate(Avg('usability')).get('usability__avg', 0.00)
    content_avg =reviews.aggregate(Avg('content')).get('content__avg', 0.00)
    if design_avg and usability_avg and content_avg is not None:
      total_sum_avg = design_avg +usability_avg+content_avg
      average_all ='{0:.2f}'.format(total_sum_avg/3)
    else:
      average_all = ' '+'is not available'  
    if request.method == 'POST':
      form = RateForm(request.POST)
      if form.is_valid():
        rate = form.save(commit=False)
        rate.user = user
        rate.project= Project.objects.get(pk=project_id)
        rate.save()
      return HttpResponseRedirect(reverse("ratings", args=[project_id]))
    else:
      form =RateForm()
    return render (request, 'rate.html' , {"form": form,"post": project, "reviews":reviews,"design_avg":design_avg,"usability_avg":usability_avg,"content_avg":content_avg,"average_all":average_all})   

class ProfileList(APIView):
  def get(self,request, format=None):
    all_profiles  = Profile.objects.all()
    serializers =ProfileSerializer(all_profiles, many=True)
    return Response(serializers.data)

  def post(self,request, format=None):
    serializers =ProfileSerializer(data=request.data)

    if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)





