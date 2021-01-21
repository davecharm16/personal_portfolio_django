from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request, *args, **kwargs):
    project = Project.objects.all()
    return render(request,'portfolio/index.html',{
        'project':project,
    })