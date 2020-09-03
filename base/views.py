from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def home(request):
    return render(request, 'base/index.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'base/projects.html',{'projects':projects})