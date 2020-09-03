from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base/index.html')

def projects(request):
    return render(request, 'base/projects.html')

def project(request):
    return render(request, 'base/project.html')

def contact(request):
    return render(request, 'base/contact.html')