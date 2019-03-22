from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.

def user_login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return HttpResponse("correct" + username + password)
        else:
            # No backend authenticated the credentials
            return HttpResponse("Incorrect" + username + password)


def signup(request):
    if request.method == "GET":
        return render(request, 'user/signup.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get("email")
        last_name = request.POST.get("lastname")
        first_name = request.POST.get("firstname")
        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        try:
            user.save()
            return HttpResponse("save successfully")
        except:
            return HttpResponse("save Unsuccessfully")


def logout(request):
    return HttpResponse("Hello, world. You're at the polls index.")
