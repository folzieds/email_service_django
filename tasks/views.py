from django.shortcuts import render, redirect

from .models import Task

# Create your views here.
def index(request):

    return render(request,"tasks/index.html", {
        "tasks": Task.objects.all()
    })

def add_task(request):

    if request.method == "POST":
        new_task = Task()
        new_task.status = False
        new_task.name = request.POST["task_name"]

        new_task.save()
    return redirect("/tasks")

def update_task(request):
    pass