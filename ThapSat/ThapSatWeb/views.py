from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html' ,{})
def updates(request):
    return render(request, 'updates.html' ,{})
