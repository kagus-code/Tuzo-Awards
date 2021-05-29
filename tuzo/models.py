from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user_name = models.CharField(max_length=30)
    profile_pic = CloudinaryField('image',null=True)
    bio = models.TextField(max_length=500, default="Bio", blank=True)
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