from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from core.models import *
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        messages.info(request, "Login failed,Please try again.")
    return render(request, 'accounts/login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone_field')
        # print(username,email)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist!")
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email already exist!")
                    return redirect('user_register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    data = Customer(user=user, phone_field=phone)
                    data.save()

                    # Code for login of user will come here
                    our_user = authenticate(username=username, password=password)
                    if our_user is not None:
                        login(request, user)
                        return redirect('/')
        else:

            messages.info(request, "Password and confirm password mismatch!")
            return redirect('user_register')
    return render(request, 'accounts/register.html')


def user_logout(request):
    logout(request)
    return redirect('/')
