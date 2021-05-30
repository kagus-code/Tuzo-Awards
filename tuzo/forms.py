from django import forms
from django.db.models import fields
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



class RateForm(forms.ModelForm):
  design =forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
  usability =forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
  content =forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
  
  class Meta:
    model = Review
    fields = ('design','usability','content')