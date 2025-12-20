from django.urls import path

from users.views import login, profile, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile')
]