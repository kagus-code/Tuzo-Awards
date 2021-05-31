from django.test import TestCase
from .models import Profile, Review,Project
from django.contrib.auth.models import User 

# Create your tests here.


class ProfileTestClass(TestCase):
  def setUp(self):
     self.profile= Profile(user_name='king',profile_pic='clodinaryfield',bio='something personal',email='ekagus@gmail.com',phone_number='0701655877')
  
  def test_instance(self):
       self.assertTrue(isinstance(self.profile, Profile))

  def test_save_profile(self):
    self.profile.save_profile()
    profiles=Profile.objects.all()
    self.assertTrue(len(profiles) > 0)

  def test_delete_username(self):
    self.profile.save_profile()
    Profile.delete_username(Profile,user_name='king')
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) == 0)  

  def test_update_profile(self):
    self.profile.save_profile()
    Profile.update_bio(user_name='king',bio='new-bio')
    self.assertTrue(Profile.objects.get(bio='new-bio'))

  def tearDown(self):
        Profile.objects.all().delete()       




class ProjectTestClass(TestCase):
   def setUp(self):
     self.project = Project(title='gallery',lannding_page='cloudinaryfield',description='amazing stuff',link='https://www.imdb.com',pub_date=2012-20-14)

   def test_instance(self):
     self.assertTrue(isinstance(self.project,Project))  

   def test_save_method(self):
     self.project.save_project()
     projects = Project.objects.all()  
     self.assertTrue(len(projects) > 0)  

   
   def test_delete_method(self):
        self.project.save_project()
        Project.delete_project(Project, title='gallery')
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)   

    

   
   def tearDown(self):
        Project.objects.all().delete()          





class ReviewTestClass(TestCase):
    def setUp(self):
      self.project = Project(title='gallery',lannding_page='cloudinaryfield',description='amazing stuff',link='https://www.imdb.com',pub_date=2012-20-14)
      self.project.save_project()


      self.review = Review(project=self.project,date=2012-20-14,
            design=10,usability=9,content=8 )

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.review, Review))


    def tearDown(self):
        Review.objects.all().delete()  
        Project.objects.all().delete() 


