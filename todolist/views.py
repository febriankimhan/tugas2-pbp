import this
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
        'username': request.user.username,
        'todolist': data
    }
    return render(request, 'todolist.html', context)

def create_task(request):
    if request.method == "POST":
        form = Task()
        form.title = request.POST.get('task_title')
        form.description = request.POST.get('task_description')
        form.date = str(datetime.date.today())
        form.user = request.user
        form.save()
        return redirect('todolist:show_todolist')

    return render(request, 'create-task.html')

def change_task_status(request, id):
    this_task = Task.objects.get(id=id)
    this_task.is_finished = not this_task.is_finished
    this_task.save()
    return redirect('todolist:show_todolist')

def delete_task(request, id):
    this_task = Task.objects.get(id=id)
    this_task.delete()
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def show_todolist_json(request):
    data_todolist = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data_todolist))

def add_todolist(request):
    if request.method == "POST":
        title = request.POST.get('task_title')
        description = request.POST.get('task_description')
        date = str(datetime.date.today())
        user = request.user

        new_task = Task(
            title=title,
            description=description,
            date=date,
            user=user
        )
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_todolist(request, id):
    this_task = Task.objects.get(id=id)
    if this_task.user == request.user:
        this_task.delete()
        return HttpResponse(b"DELETED", status=201)

    return HttpResponseNotFound()