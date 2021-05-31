from django.db.models import fields
from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_name', 'bio', 'profile_pic')

class ProjectSerializers(serializers.ModelSerializer):
  class Meta:
    model =Project
    fields = ('title','lannding_page','description','link','pub_date','Publisher')
