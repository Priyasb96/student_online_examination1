from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return render(request, 'exam1\login.html')

def home(request):
     return render(request, 'exam1/register.html')

# def home(request):
#     return render(request, 'exam1/dashboard.html')

