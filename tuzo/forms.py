from django import forms
from .models import Profile,Project,Review, RATE_CHOICES
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['pub_date','Publisher']


class UpdateProfileForm(forms.ModelForm):

  class Meta:
    model = Profile

    exclude=['user','user_name','email']