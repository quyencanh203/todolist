from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from . import models

def index(request):
    tasks = models.Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)

def detail(request, id):
    task = models.Task.objects.get(id=id)
    context = {'task': task}
    return render(request, 'todo/detail.html', context)

def update(request, id):
    if request.method == 'POST':
        task = models.Task.objects.get(id=id)
        task.done = 'done' in request.POST
        task.save()
    return redirect('/todo')