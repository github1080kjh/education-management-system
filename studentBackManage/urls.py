"""studentBackManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstPage/', views.first_page),
    path('loginTest/', views.login_test),
    path('studentLogin/', views.student_login),
    path('teacherLogin/', views.teacher_login),
    path('adminLogin/', views.admin_login),
    path('adminPage/', views.admin_page),
    path('studentPage/', views.student_page),
    path('teacherPage/', views.teacher_page),
    path('schoolIntroduction/', views.school_introduction),
    path('addTeacher/', views.add_teacher),
    path('addStudent/', views.add_student),
    path('addAdmin/', views.add_admin),
    path('addClass/', views.add_class),
]
