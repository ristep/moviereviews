from django.urls import path

from accounts import views

urlpatterns = [
   path('about/', views.about,  name='about'),
   path('signup/', views.signup, name='signup'),
   path('signupaccount/', views.signupaccount, name='signupaccount'),
   path('logout/', views.logoutaccount, name='logoutaccount'),
   path('login/', views.loginaccount, name='loginaccount'),
]