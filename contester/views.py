from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    return render(request, 'contester/index.html')

def home(request):
    current_user = request.user
    tasks = Task.objects.all()
    return render(request, 'contester/home.html', {'user':current_user,'tasks':tasks})

def getTaskById(request,id):
    task = Task.objects.get(pk=id)
    return render(request,'contester/task.html', {'task':task})

def loginRed(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('contester:homepage')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'registration/register.html', context)