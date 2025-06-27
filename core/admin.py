from django.contrib import admin
from .models import Project,ContactMessage

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['subtitle']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'submitted_at']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactMessage, ContactAdmin)