from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html' ,{})
def updates(request):
    return render(request, 'updates.html' ,{})
def departments(request):
    return render(request, 'departments.html' ,{})
def subsystems(request):
    return render(request, 'subsystems.html' ,{})
def social(request):
    return render(request, 'social.html' ,{})
