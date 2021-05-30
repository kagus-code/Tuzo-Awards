from django.urls import path, re_path



from . import views



urlpatterns = [

  re_path(r'^$', views.landing,name='landingPage'),
  re_path(r'^upload_project/', views.upload_project, name='upload_project'),
]