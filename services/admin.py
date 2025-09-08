from django.contrib import admin
from .models import Service, ServiceInquiry

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)

@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone', 'service', 'created')
    list_filter = ('service', 'created')
    search_fields = ('name', 'email', 'message')
