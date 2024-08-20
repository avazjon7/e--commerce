from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.safestring import mark_safe

from customers.models import Customer
#
# admin.site.register(User)
admin.site.unregister(Group)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display: tuple = ('full_name', 'email', 'phone', 'address')  # preview_image
    search_fields: list = ['full_name', 'email', 'address']
    list_filter: list = ['address']
    prepopulated_fields: dict = {'slug': ('full_name',)}