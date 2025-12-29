from django.shortcuts import redirect, render
from django.views import View
from .forms import ThinkUserForm, ThinkAuthForm
from django.contrib.auth import login

# Create your views here.

class Login(View):
    def get(self, request):
        form = ThinkAuthForm()
        return render(request, 'user/login.html', context={'form':form})

    def post(self, request):
        form = ThinkAuthForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('board')
        return render(request, 'user/login.html', context={'form':form})



class SignUp(View):
    def get(self, request):
        form = ThinkUserForm()
        return render(request, 'user/signup.html', context={'form':form})
    
    def post(self, request):
        form = ThinkUserForm(request, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'user/signup.html', context={'form':form})


class Profile(View):
    def get(self, request):
        return render(request, 'user/profile.html')