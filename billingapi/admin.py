from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "first_name", "last_name", "email"]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["id", "total_amount", "timestamp"]
