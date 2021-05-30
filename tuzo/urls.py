from django.urls import path, re_path



from . import views



urlpatterns = [

  re_path(r'^$', views.landing,name='landingPage'),
  re_path(r'^upload_project/', views.upload_project, name='upload_project'),
  re_path(r'^edit_profile/(?P<userId>\d+)/$', views.edit_profile, name='edit_profile'),
  re_path(r'^profile/(?P<userId>\d+)/$', views.user_profile, name='profile_page'),
  re_path(r'^search/', views.search_results, name='search_results'),
  re_path(r'^ratings/(?P<project_id>\d+)/$', views.rate, name='rate'),

]
