from django.contrib import admin
from .models import Product,ProductInquiry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)

@admin.register(ProductInquiry)
class ProductInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone', 'product', 'created')
    list_filter = ('product', 'created')
    search_fields = ('name', 'email', 'message')