from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from base.models import UserModel
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'image', 'covid_positive', 'covid_contact']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
