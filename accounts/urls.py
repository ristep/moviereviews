from django.urls import path

from accounts import views

urlpatterns = [
   path('about/', views.about,  name='about'),
   path('signup/', views.signup, name='signup'),
   path('signupaccount/', views.signupaccount, name='signupaccount'),
]