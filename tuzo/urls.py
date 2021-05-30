from django.urls import path, re_path



from . import views



urlpatterns = [

  re_path(r'^$', views.landing,name='landingPage'),
  re_path(r'^upload_project/', views.upload_project, name='upload_project'),
  # re_path(r'^edit_profile/(?P<userId>\d+)/$', views.edit_profile, name='edit_profile'),
  re_path(r'^profile/(?P<userId>\d+)/$', views.user_profile, name='profile_page'),
]