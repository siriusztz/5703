from django.db import models


# Create your models here.

class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    faculty = models.CharField(max_length=200, null=True)  # enroll_faculty
    email_ini = models.EmailField(null=True)
    email_per = models.EmailField(null=True)
    mobile_num = models.IntegerField(null=True)
    course = models.CharField(max_length=200, null=True)  # stream
    course_code = models.CharField(max_length=200, null=True)  # stream code
    course_type = models.CharField(max_length=200, null=True)
    course_type_name = models.CharField(max_length=200, null=True)
    citizen_type = models.CharField(max_length=200, null=True)
    citizen_country = models.CharField(max_length=200, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    last_enrol_date = models.DateField(null=True)
    address = models.DateField(null=True)
    attend_mode = models.CharField(max_length=200, null=True)


class Unit(models.Model):
    code = models.CharField(max_length=200, null=True)  # UOS code
    name = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    semester = models.CharField(max_length=200, null=True)
    level = models.CharField(max_length=200, null=True)


class Grade(models.Model):
    student = models.IntegerField(null=True)
    unit = models.IntegerField(null=True)
    status = models.CharField(max_length=200, null=True)
    mark = models.IntegerField(null=True)
    grade = models.CharField(max_length=200, null=True)
    aam = models.IntegerField(null=True)
    wam = models.IntegerField(null=True)
    Credit_attemp = models.IntegerField(null=True)
    Credit_passed = models.IntegerField(null=True)
