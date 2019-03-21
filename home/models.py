from django.db import models


# Create your models here.

class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)  # enroll_faculty
    email_ini = models.EmailField()
    email_per = models.EmailField()
    mobile_num = models.IntegerField()
    course = models.CharField(max_length=200)  # stream
    course_code = models.CharField(max_length=200)  # stream code
    course_type = models.CharField(max_length=200)
    course_type_name = models.CharField(max_length=200)
    citizen_type = models.CharField(max_length=200)
    citizen_country = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    last_enrol_date = models.DateField()
    address = models.DateField()
    attend_mode = models.CharField(max_length=200)


class Unit(models.Model):
    code = models.CharField(max_length=200)  # UOS code
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
    level = models.CharField(max_length=200)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    grade = models.IntegerField()
    aam = models.IntegerField()
    wam = models.IntegerField()
    Credit_attemp = models.IntegerField()
    Credit_passed = models.IntegerField()
