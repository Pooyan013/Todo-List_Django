from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm

def index(request):
    form = TaskForm
    tasks = Task.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    return render(request,"tasks.html", context={
        "tasks":tasks,
        "TaskForm":form,
    })

def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"update.html", context={
        "TaskForm":form,
    })


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
    return redirect("/")

    return render(request, "delete.html",context = {task:"task"})