from asyncio import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from todolist.models import Task
from todolist.forms import TaskForm
# Create your views here.

def todolist(request):
    return render(request, "todolist_ajax.html")

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
    'list_todolist': data_todolist,
    }
    return render(request, "todolist.html", context)

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
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')


def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'create-task.html', context)
    

@login_required(login_url='/todolist/login/')
def update_data(request):
    todo = Task.objects.get(id=request.POST["id"])
    todo.is_finished = not(todo.is_finished)
    todo.save()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def delete_data(request):
    todo = Task.objects.get(id=request.POST["id"])
    todo.delete()
    return redirect('todolist:show_todolist')

def get_todolist_json(request):
    todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist))

def add_todolist_item(request):
    if request.method == 'POST':
        date = request.POST.get("date")
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_todolist = Task(date=date, title=title, description=description)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()