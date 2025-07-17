# from django.shortcuts import render, redirect 
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import get_user_model
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import RegisterForm
# import random

# User = get_user_model()

# # Store OTPs temporarily
# otp_store = {}

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             otp = str(random.randint(100000, 999999))
#             otp_store[username] = otp
#             request.session["otp_user"] = username
#             print(f"OTP for {username}: {otp}")
#             messages.info(request, "OTP sent. Check terminal.")
#             return redirect('auth_page')
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('auth_page')
#     return redirect('auth_page')


# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Registration successful! You can now log in.")
#             return redirect('auth_page')
#     else:
#         form = RegisterForm()
#     return render(request, 'exam1/auth.html', {"form": form, "show": "register-form"})


# def verify_otp(request):
#     username = request.session.get("otp_user")
#     if request.method == "POST":
#         entered_otp = request.POST.get("otp")
#         actual_otp = otp_store.get(username)
#         if entered_otp == actual_otp:
#             user = User.objects.get(username=username)
#             login(request, user)
#             request.session.pop("otp_user", None)
#             otp_store.pop(username, None)

#             if user.role == 'student':
#                 return redirect('student_dashboard')
#             elif user.role == 'invigilator':
#                 return redirect('invigilator_dashboard')
#             else:
#                 messages.warning(request, "Unknown role. Contact admin.")
#                 return redirect('auth_page')
#         else:
#             messages.error(request, "Invalid OTP. Please try again.")
#             return redirect('auth_page')
#     return render(request, 'exam1/auth.html', {"show": "otp-form"})


# def auth_page(request):
#     form = RegisterForm()
#     return render(request, "exam1/auth.html", {"form": form, "show": "login-form"})


# @login_required
# def student_dashboard(request):
#     return render(request, 'student_dashboard.html')


# @login_required
# def invigilator_dashboard(request):
#     return render(request, 'invigilator_dashboard.html')


# # 🔥 Removed the unused home_view
# # def home_view(request):
# #     return render(request, 'home.html')  # ❌ Not needed

# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

User = get_user_model()

@login_required
def dashboard_view(request):
    return render(request, "exam1/dashboard.html", {"user": request.user})

def generate_otp():
    return str(random.randint(100000, 999999))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "exam1/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]

        if password != confirm:
            return render(request, "exam1/register.html", {"error": "Passwords do not match"})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()

        otp = generate_otp()
        request.session["otp"] = otp
        request.session["user_to_verify"] = username

        send_mail(
            "Your OTP",
            f"Here is your OTP: {otp}",
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )
        return redirect("verify_otp")

    return render(request, "exam1/register.html")

def otp_view(request):
    if request.method == "POST":
        entered = "".join([request.POST.get(f"digit{i}") for i in range(1, 7)])
        session_otp = request.session.get("otp")
        username = request.session.get("user_to_verify")

        if entered == session_otp and username:
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()
            login(request, user)
            return redirect("dashboard")

    return render(request, "exam1/otp.html")

def resend_otp(request):
    username = request.session.get("user_to_verify")
    if username:
        user = User.objects.get(username=username)
        otp = generate_otp()
        request.session["otp"] = otp
        send_mail(
            "Your New OTP",
            f"Your new OTP is: {otp}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )
    return redirect("verify_otp")

# def auth_success(request):
#     return render(request, "exam1/auth_success.html")

def auth_page(request):
    return render(request, 'exam1/auth.html')  # Make sure you have an auth.html template

@csrf_protect
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")