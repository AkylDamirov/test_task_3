from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout
# Create your views here.

def index(request):
    return render(request, 'task_app/index.html')

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')

    form = NewUserForm
    return render(request, 'registration/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')


