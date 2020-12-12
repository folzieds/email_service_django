from django.shortcuts import render, redirect

from .models import Task

# Create your views here.
def index(request):

    return render(request,"tasks/index.html", {
        "tasks": Task.objects.all()
    })

def add_task(request):
    return redirect("tasks/index.html")