from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token



from . import views



urlpatterns = [

  re_path(r'^$', views.landing,name='landingPage'),
  re_path(r'^upload_project/', views.upload_project, name='upload_project'),
  re_path(r'^edit_profile/(?P<userId>\d+)/$', views.edit_profile, name='edit_profile'),
  re_path(r'^profile/(?P<userId>\d+)/$', views.user_profile, name='profile_page'),
  re_path(r'^search/', views.search_results, name='search_results'),
  re_path(r'^ratings/(?P<project_id>\d+)/$', views.rate_project, name='ratings'),
  re_path(r'^api/profile/$', views.ProfileList.as_view()),
  re_path(r'^api-token-auth/', obtain_auth_token),

]
