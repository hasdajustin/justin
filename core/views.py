from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def portfolio(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'core/portfolio.html', {'projects': projects})

def contact(request):
    return render(request, 'core/contact.html')