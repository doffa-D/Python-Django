from django.shortcuts import render

# Create your views here.

def django_history(request):
    return render(request,'Django_history.html')

def django_display(request):
    return render(request,'Django_display.html')

def django_templates(request):
    return render(request,'Django_template.html')

def django_nav(request):
    return render(request , 'nav.html')