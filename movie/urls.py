from django.urls import path

from movie import views

urlpatterns = [
   path('', views.home, name='doma' ),
   path('home/', views.home, name="home"),
   path('about/', views.about,  name='about'),
   path('signup/', views.signup, name='signup'),
]