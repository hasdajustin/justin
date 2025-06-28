from django import forms
from .models import Project, ContactMessage, HireRequest

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'subtitle', 'description', 'preview_link', 'live_link']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message...', 'rows': 5}),
        }
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }


class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = ['full_name', 'email', 'project_type', 'budget', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'project_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Portfolio Website, Ecommerce Site'}),
            'budget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }