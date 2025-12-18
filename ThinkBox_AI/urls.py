"""
URL configuration for ThinkBox_AI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workspaces.views import dashboard, members
from documents.views import document
from chats.views import chat
from users.views import login, signup, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workspace/', dashboard, name='board'),
    path('members/', members, name='member'),
    path('doc/', document, name='docs'),
    path('chat/', chat, name='chat'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
]
