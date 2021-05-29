from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    user_name = models.CharField(max_length=30)
    profile_pic = CloudinaryField('image',null=True)
    bio = models.TextField(max_length=500,  blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def save_profile(self):
        self.save()

    def delete_username(self, user_name):
        self.objects.filter(user_name=user_name).delete()

    @classmethod
    def update_username(cls,user_name,new_name):
        update = Profile.objects.filter(user_name=user_name).update(user_name=new_name)
        return update

    @classmethod
    def update_bio(cls,user_name,bio):
        update = Profile.objects.filter(user_name=user_name).update(bio=bio)
        return update

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['user_name'] 

class Project(models.Model):
  title = models.CharField(max_length=50)
  lannding_page = CloudinaryField('image',null=True)
  description = models.TextField(max_length=500,  blank=True)
  link =  models.URLField(max_length = 200)
  pub_date = models.DateTimeField(auto_now_add=True)

  def save_project(self):
    self.save()

  def delete_project(self,title):
    delete =self.objects.filter(title=title).delete() 
    return delete 

  def __str__(self):
        return self.title

  class Meta:
        ordering = ['-pub_date']     
