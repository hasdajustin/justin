from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def portfolio(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'core/portfolio.html', {'projects': projects})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def hireme(request):
    return render(request, 'core/hireme.html')