from django.shortcuts import render

# Create your views here.

def home(r):
    return render(r,'resumeApp/home.html')

def resume(r):
    return render(r,'resumeApp/resume.html')

def projects(r):
    return render(r,'resumeApp/projects.html')

def hobbies(r):
    return render(r,'resumeApp/hobbies.html')

def contact(r):
    return render(r,'resumeApp/contact.html')