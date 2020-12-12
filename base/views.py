from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from base.models import UserModel
from login.forms import UserForm


@login_required(login_url='sign_in')
def home(request):
    user = request.user
    user_extended = UserModel.objects.get(user=user)
    friends = user_extended.friends.all()

    alert_list = []
    for friend in friends:
        if friend.covid_positive:
            alert_list.append(f'{friend.first_name} {friend.last_name}')

    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('check', False):
            user_extended.covid_contact = True
            user_extended.save()
        alert_list = []

    context = {
        'user': user,
        'user_extended': user_extended,
        'friends': friends,
        'alerts': alert_list
    }
    return render(request, 'home.html', context)


@login_required(login_url='sign_in')
def friend_search(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            users = UserModel.objects.all()

            user_names = [f'{user.first_name} {user.last_name}' for user in users]
            name_searched = request.POST.get('name')

            user_list = []
            for user_name, user in zip(user_names, users):
                if name_searched in user_name:
                    if not request.user == user.user:
                        user_list.append(user)

            context = {
                'users': user_list,
            }
            return render(request, 'search.html', context)
        elif request.POST.get('user'):
            friend_to_add = UserModel.objects.get(pk=request.POST.get('user'))
            user_extended = UserModel.objects.get(user=request.user)
            user_extended.friends.add(friend_to_add)
            user_extended.save()

            return redirect('home')

    return render(request, 'search.html')


@login_required(login_url='sign_in')
def edit_profile(request):
    user = UserModel.objects.get(user=request.user)
    if request.method == 'GET':
        form = UserForm(instance=user)
        return render(request, 'edit.html', {'form': form})
    else:
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'edit.html', {'form': form})


@login_required(login_url='sign_in')
def friends_list(request):
    user = UserModel.objects.get(user=request.user)
    friends = user.friends.all()

    context = {'friends': friends}
    return render(request, 'friends.html', context)
