from django.urls import path

from movie import views

urlpatterns = [
   path('', views.home, name='doma' ),
   path('home/', views.home, name="home"),
   path('<int:movie_id>', views.detail, name='detail'),
]