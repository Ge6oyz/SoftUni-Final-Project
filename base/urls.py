from django.urls import path
from base.views import home, friend_search, edit_profile, friends_list

urlpatterns = [
    path('', home, name='home'),
    path('search/', friend_search, name='friend_search'),
    path('edit/', edit_profile, name='edit'),
    path('friends/', friends_list, name='friends')
]

