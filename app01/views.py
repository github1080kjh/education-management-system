from django.shortcuts import render, HttpResponse, redirect
from app01 import models
import datetime
import requests
import os


# Create your views here.


# 首页的视图函数
def first_page(req):
    return render(req, 'first_page.html')


# 学生登录页面的函数
def student_login(req):
    error_message = ''
    if req.method == 'POST':

        # 是否记住账号密码
        # remember = req.POST.get('remember', None)
        # print(remember)

        user_name = req.POST.get('name', None)
        user_pwd = req.POST.get('password', None)

        # 从数据库拿数据对比用户账户信息
        find_result = models.StudentLogin.objects.filter(userName=user_name, userPwd=user_pwd).count()
        if find_result:

            req = redirect('/studentPage/?name={}'.format(user_name))
            req.set_cookie('user_name', user_name)
            return req

        error_message = 'input error, please input again！'
    return render(req, 'student_login.html', {'error_message': error_message})


# 老师登录页面的函数
def teacher_login(req):
    error_message = ''
    if req.method == 'POST':
        user_name = req.POST.get('name', None)
        user_pwd = req.POST.get('password', None)
        # 从数据库拿数据对比用户账户信息
        find_result = models.TeacherLogin.objects.filter(userName=user_name, userPwd=user_pwd).count()
        if find_result:
            req = redirect('/teacherPage/?name={}'.format(user_name))
            req.set_cookie('user_name', user_name)
            return req

        error_message = 'input error, please input again！'
    return render(req, 'teacher_login.html', {'error_message': error_message})


# 管理员登录页面的函数
def admin_login(req):
    error_message = ''
    if req.method == 'POST':
        user_name = req.POST.get('name', None)
        user_pwd = req.POST.get('password', None)
        # 从数据库拿数据对比用户账户信息
        find_result = models.Administrator.objects.filter(userName=user_name, userPwd=user_pwd).count()
        if find_result:
            req = redirect('/adminPage/?name={}'.format(user_name))
            req.set_cookie('user_name', user_name)
            return req

        error_message = 'input error, please input again！'
    return render(req, 'admin_login.html', {'error_message': error_message})


# 测试登录页面
def login_test(req):
    return render(req, 'login_templates.html')


# admin登录后显示页面的函数
def admin_page(req):
    cookie_value = req.COOKIES.get('user_name')
    if cookie_value:
        username = req.GET.get('name', None)
        teacher_obj = models.Teacher.objects.all()
        student_obj = models.Student.objects.all()
        class_obj = models.Classes.objects.all()
        admin_obj = models.Administrator.objects.all()
        suggestive_content_obj = models.Suggestive.objects.all()
        college_obj = models.College.objects.all()
        return render(req, 'admin_page.html',
                      {'username': username, 'admin_obj': admin_obj, 'class_obj': class_obj, 'teacher_obj': teacher_obj,
                       'student_obj': student_obj, 'college_obj': college_obj, 'suggestive_content_obj': suggestive_content_obj})
    return render(req, 'admin_login.html', {'error_message': 'time out!'})


# 学生登录后显示页面的函数
def student_page(req):
    cookie_value = req.COOKIES.get('user_name')
    student_obj = models.Student.objects.all()
    # print(student_obj)
    if cookie_value:
        username = req.GET.get('name', None)
        # print(username)
        person_obj = models.Student.objects.filter(name=username)
        # print(person_obj)
        if req.method == 'POST':
            # name = req.GET.get('name')
            now_time = str(datetime.datetime.now()).split('.')[0]
            suggestive_content = req.POST.get('suggestive_info', None)
            submit_person = req.POST.get('submit_name', None)
            models.Suggestive.objects.create(
                suggestive_content=suggestive_content,
                submit_person_id=submit_person,
                submit_time=now_time
            )
            name = models.Student.objects.get(id=submit_person).name
            # print(name)
            return redirect('/studentPage/?name={}'.format(name))
        return render(req, 'student_page.html', {'username': username, 'person_obj': person_obj, 'student_obj': student_obj})
    return render(req, 'student_login.html', {'error_message': 'time out!'})


# 老师登录后显示页面的函数
def teacher_page(req):
    cookie_value = req.COOKIES.get('user_name')

    if cookie_value:
        username = req.GET.get('name', None)
        class_obj = models.Classes.objects.all()
        student_obj = models.Student.objects.all()
        suggestive_obj = models.Suggestive.objects.all()

        teacher_obj = models.Teacher.objects.get(name=username)

        classes_list = []   # 用于存储登录用户所带的班级名称
        for classes in teacher_obj.classes_set.all():    # 通过外键的反向查找
            classes_list.append(classes.name)
        # print(teacher_obj.name, teacher_obj.college.name, teacher_obj.classes_set.all())

        # 用于存储登录用户的个人信息
        teacher_info_list = [teacher_obj.name, teacher_obj.college.name, classes_list]
        return render(req, 'teacher_page.html', {'suggestive_obj': suggestive_obj, 'class_obj': class_obj, 'student_obj': student_obj, 'username': username, 'teacher_info_list': teacher_info_list})
    return render(req, 'teacher_login.html', {'error_message': 'time out!'})


# 学校介绍页面的函数
def school_introduction(req):
    return render(req, 'school_introduction.html')


# 添加教师
def add_teacher(req):
    college_obj = models.College.objects.all()
    if req.method == 'POST':
        name = req.POST.get('username', None)
        password = req.POST.get('password', None)
        college = req.POST.get('college', None)
        models.TeacherLogin.objects.create(userName=name, userPwd=password)
        models.Teacher.objects.create(name=name, college_id=college)
        return redirect('/adminPage/')
    return render(req, 'add_teacher.html', {'college_obj': college_obj})


# 添加学生
def add_student(req):
    class_obj = models.Classes.objects.all()
    college_obj = models.College.objects.all()
    if req.method == 'POST':
        name = req.POST.get('username', None)
        password = req.POST.get('password', None)
        age = req.POST.get('age', None)
        id_number = req.POST.get('id_number', None)
        college = req.POST.get('college', None)
        class_name = req.POST.get('classes', None)
        models.Student.objects.create(
            name=name,
            age=age,
            id_number=id_number,
            college_id=college,
            classes_id=class_name
        )
        models.StudentLogin.objects.create(userName=name, userPwd=password)

        return redirect('/adminPage/')
    return render(req, 'add_student.html', {'class_obj': class_obj, 'college_obj': college_obj})


# 添加管理员
def add_admin(req):
    if req.method == 'POST':
        name = req.POST.get('username', None)
        password = req.POST.get('password', None)
        models.Administrator.objects.create(userName=name, userPwd=password)
        return redirect('/adminPage/')
    return render(req, 'add_admin.html')


# 添加班级
def add_class(req):
    leader_obj = models.Teacher.objects.all()
    if req.method == 'POST':
        class_name = req.POST.get('class_name', None)
        leader = req.POST.get('leader', None)
        models.Classes.objects.create(name=class_name, leader_id=leader)
        return redirect('/adminPage/')

    return render(req, 'add_class.html', {'leader_obj': leader_obj})