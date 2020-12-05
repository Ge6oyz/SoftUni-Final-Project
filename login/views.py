from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from base.models import UserModel
from login.forms import CreateUserForm


def sign_up_view(request):
    if request.method == "GET":
        form = CreateUserForm()
        context = {
            'form': form
        }
        return render(request, 'sign_up.html', context)
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_created = User.objects.get(pk=user.id)
            UserModel(user=user_created, first_name=user.first_name, last_name=user.last_name).save()
            messages.success(request, f'Account created successfully')

            return redirect('sign_in')

        context = {
            'errors': form.errors,
            'form': CreateUserForm()
        }

        return render(request, 'sign_up.html', context)


def sign_in_view(request):
    if request.method == "GET":
        context = {}
        return render(request, 'sign_in.html', context)
    else:

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
        return redirect('sign_in')


def sign_out_view(request):
    logout(request)
    return redirect('sign_in')
