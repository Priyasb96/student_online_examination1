from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def register_view(request):
     form = RegisterForm()
     if request.method == 'POST':
          form = RegisterForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, "Register Successful")
               return redirect('login')
     return render(request, 'exam1/register.html',{'form': form})

def login_view(request):
     if request.method == "POST":
          username = request.POST.get("username")
          password = request.POST.get("password")

          user = authenticate(request, username=username, password=password)
          if user:
               login(request,user)
               return redirect('admin')
          else:
               messages.error(request, "Invalid username or password.")
               return redirect('login')
     return render(request, 'exam1/login.html')

def verify_otp(request):
      messages.info(request, "OTP verification placeholder.")
      return redirect('admin')

# def logout_view(request):
#       logout
#       return render(request, 'exam1/dashboard.html')
