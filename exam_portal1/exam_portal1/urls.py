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
# from django.contrib import admin
# from django.urls import path, include
# from exam1 import views 

# urlpatterns = [
#     path('', views.auth_page, name='auth_page'),
#     path('admin/', admin.site.urls),
#     path('register/', views.register_view, name='register'),    # ✅ Make sure this is correct
#     path('verify/',views.verify_otp,name='verify_otp'),
#     path('login/',views.login_view, name='login'),
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('exam1.urls')),  # ✅ Connect your app here
# ]


# from django.contrib import admin
# from django.urls import path, include
# from exam1 import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('exam1.urls')),
#     path('', views.home_view, name='home'),  # Home page route
#     path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard route
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam1.urls')),
]
