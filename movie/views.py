from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def home(request):
   searchTerm = request.GET.get('searchMovie')
   movies = Movie.objects.all()
   return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies} )

def about(request):
   return HttpResponse("About Page!")

def signup(request):
 email = request.GET.get('email')
 return render(request, 'signup.html', {'email':email})