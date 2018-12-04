from django.db import models

# Create your models here.


# 学生表
class Student(models.Model):
    name = models.CharField(max_length=40, null=False)
    age = models.CharField(max_length=12, null=False)
    classes = models.ForeignKey('Classes', 'id', null=False)     # 学生所属的班级，外键关联关系
    college = models.ForeignKey('College', 'id', null=False)    # 学生所属的学院
    id_number = models.CharField(max_length=30, null=False)


# 班级表
class Classes(models.Model):
    name = models.CharField(max_length=20, null=False)
    leader = models.ForeignKey('Teacher', 'id', null=False)    # 班级对应的班主任


# 教师表
class Teacher(models.Model):
    name = models.CharField(max_length=40, null=False)
    college = models.ForeignKey('College', 'id', null=False)         # 是属于哪个学院的教师


# 学院表
class College(models.Model):
    name = models.CharField(max_length=20, null=False)


# 管理员表
class Administrator(models.Model):
    userName = models.CharField(max_length=40, null=False)
    userPwd = models.CharField(max_length=20, null=False)


# 学生登录表
class StudentLogin(models.Model):
    userName = models.CharField(max_length=40, unique=True, null=False)
    userPwd = models.CharField(max_length=20, null=False)


# 教师登录表
class TeacherLogin(models.Model):
    userName = models.CharField(max_length=40, unique=True, null=False)
    userPwd = models.CharField(max_length=20, null=False)


# 建议提交表
class Suggestive(models.Model):
    submit_person = models.ForeignKey('Student', 'id', null=False)    # 提交人
    suggestive_content = models.CharField(max_length=200, null=False)  # 建议内容
    submit_time = models.CharField(max_length=64, null=False)  # 提交时间
