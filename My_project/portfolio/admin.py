from django.contrib import admin
from .models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reason', 'message', 'submitted_at')
    search_fields = ('name', 'email', 'reason')
    list_filter = ('reason', 'submitted_at')