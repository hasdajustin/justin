from django.contrib import admin
from .models import Project,ContactMessage,HireRequest

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['subtitle']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'submitted_at']

class HireRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'project_type', 'budget']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactMessage, ContactAdmin)
admin.site.register(HireRequest, HireRequestAdmin)