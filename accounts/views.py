from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm

# Create your views here.
def about(request):
    return HttpResponse("About Page!")


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})


def signupaccount(request):
   if request.method == 'GET':
      return render(request, 'signupaccount.html', {'form':UserCreateForm})
   else:
      if request.POST['password1'] == request.POST['password2']:
         try:
            user = User.objects.create_user( request.POST['username'], password = request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
         except IntegrityError:
            return render(request,'signupaccount.html', {'form':UserCreateForm,'error':'Username already taken. Choose new username.'})
      else:
         return render( request, 'signupaccount.html', {'form':UserCreateForm, 'error':'Passwords do not match'} )  
