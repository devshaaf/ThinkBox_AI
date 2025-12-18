from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'workspace/dashboard.html')


def members(request):
    return render(request, 'workspace/members.html')