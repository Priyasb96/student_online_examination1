"""
URL configuration for exam_portal1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('verify/', views.verify_otp, name='verify_otp'),
#     path('login/', views.login_view, name='login'),
# ]

# from django.urls import path
# from . import views
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('', views.login_view, name='login_view'),
#     path('register/', views.register_view, name='register_view'),
#     path('verify-otp/', views.verify_otp, name='verify_otp'),         # ✅ Needed for OTP verification
#     path('auth/', views.auth_page, name='auth_page'),                 # ✅ Needed to render auth.html

#     path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
#     path('invigilator/dashboard/', views.invigilator_dashboard, name='invigilator_dashboard'),
#     path('logout/', LogoutView.as_view(next_page='login_view'), name='logout'),
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='home'),  # 👈 This makes dashboard the homepage
#     path('auth/', views.auth_page, name='auth_page'),
#     path('login/', views.login_view, name='login_view'),
#     path('register/', views.register_view, name='register_view'),
#     path('verify-otp/', views.verify_otp, name='verify_otp'),
#     path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
#     path('invigilator-dashboard/', views.invigilator_dashboard, name='invigilator_dashboard'),
#     path('dashboard/', views.dashboard, name='dashboard'),  # optional if you still want /dashboard/
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Must match 'login' name
    path('otp/', views.otp_verify, name='otp_verify'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

]
