from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html', {})

def contact_us(request):
    return render(request, 'home/contact_us.html', {})

def about_us(request):
    return render(request, 'home/about_us.html', {})

def ideas(request):
    return render(request, 'home/ideas.html', {})
