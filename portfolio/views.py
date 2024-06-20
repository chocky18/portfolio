from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def resume(request):
    return render(request, 'portfolio/resume.html')



def details(request):
    return render(request, 'portfolio/details.html')
